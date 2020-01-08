import re
import json
import time
import subprocess
import shlex
import platform
from pathlib import Path
from operator import itemgetter

import pytest


WIN = platform.system() == 'Windows'
HOST = f"{platform.node() if WIN else '0.0.0.0'}:8080"

SYSTEM_SUFFIXES = ('_win.txt', '_unix.txt')
CURRENT_SYSTEM_SUFFIX = '_win.txt' if WIN else '_unix.txt'


def parse_response(text):
    text = text.replace('\r\n', '\n')
    head, body = text.split('\n\n') if '\n\n' in text else (text, None)

    head = head.replace('application/json; charset=UTF-8', 'application/json')
    head_lines = head.splitlines()
    head_lines = [h for h in head_lines if not h.lower().startswith('date:')]

    status = int(re.search(r' (\d{3}) ', head_lines[0]).group(1))
    headers = head_lines[1:]
    body = (body.strip() if '/json' in head else body) if body and body.strip() else None
    body_json = json.loads(body) if body and '/json' in head else None

    return dict(status=status, headers=headers, body=body, body_json=body_json)


def parse_test(text, filename=None):
    lines = text.splitlines()

    command = replace_host(lines[0][2:])
    response = parse_response('\n'.join(lines[1:]) + '\n')

    # Temporarily parse headers into a dict
    headers = dict([header.split(': ') for header in response['headers']])

    # Replace host in the Location header which usually contains a link
    if 'Location' in headers:
        headers['Location'] = replace_host(headers['Location'])

    # Because we'll be altering body and the Content-Length header a few lines
    # below, let's verify first that the original file has it right.
    if response['body'] is not None:
        assert int(headers['Content-Length']) == len(response['body']), filename

        # The body can contain links, so we must replace host even there. That
        # changes the Content-Length though, so it must be re-calculated.
        response['body'] = replace_host(response['body'])
        headers['Content-Length'] = len(response['body'])

        # We must update the parsed JSON body as well
        if response['body_json'] is not None:
            response['body_json'] = json.loads(response['body'])

    # Squash headers back
    response['headers'] = [f'{name}: {value}' for name, value
                           in headers.items()]

    return dict(command=command, response=response)


def replace_host(text):
    return (text.replace('0.0.0.0:8080', HOST)
                .replace('MY-COMPUTER:8080', HOST)
                .replace('api.example.com', HOST))


def is_test(basename):
    if basename.startswith(('test', 'example')):
        if basename.endswith(SYSTEM_SUFFIXES):
            return basename.endswith(CURRENT_SYSTEM_SUFFIX)
        return True
    return False


def generate(dir):
    for path in sorted(dir.iterdir()):
        if not path.is_dir() or path.name == '__pycache__':
            continue

        tests = [
            parse_test(f.read_text(), filename=str(f.resolve()))
            for f in sorted(path.iterdir()) if is_test(f.name)
        ]
        yield dict(src=path, name='code/server/' + path.name, tests=tests)


def run_test(command):
    client = subprocess.run(shlex.split(command),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    return parse_response(client.stdout.decode('utf-8'))


test_batches = list(generate(Path(__file__).parent))


@pytest.mark.parametrize('test_batch', test_batches, ids=itemgetter('name'))
def test_code_works(test_batch):
    server = subprocess.Popen(['waitress-serve', 'index:app'],
                              cwd=test_batch['src'])
    time.sleep(0.5)
    try:
        tests = [
            (test['command'], run_test(test['command']), test['response'])
            for test in test_batch['tests']
        ]
    finally:
        server.terminate()

    for command, response, expected_response in tests:
        print(command)
        assert response['status'] == expected_response['status']
        for header in expected_response['headers']:
            assert header in response['headers']
        if response['body_json']:
            assert response['body_json'] == expected_response['body_json']
        else:
            assert response['body'] == expected_response['body']
