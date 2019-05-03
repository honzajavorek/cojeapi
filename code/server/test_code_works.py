import re
import json
import time
import subprocess
import shlex
from pathlib import Path
from operator import itemgetter

import pytest


def parse_response(text):
    text = text.replace('\r\n', '\n')
    head, body = text.split('\n\n') if '\n\n' in text else (text, None)

    head = head.replace('application/json; charset=UTF-8', 'application/json')
    head_lines = head.splitlines()
    head_lines = [h for h in head_lines if not h.lower().startswith('date:')]

    status = int(re.search(r' (\d{3}) ', head_lines[0]).group(1))
    headers = head_lines[1:]
    body = body.strip() if body and body.strip() else None
    body_json = json.loads(body) if body and '/json' in head else None

    return dict(status=status, headers=headers, body=body, body_json=body_json)


def parse_test(text):
    lines = text.splitlines()
    command = lines[0][2:].replace('api.example.com', '0.0.0.0:8080')
    response = parse_response('\n'.join(lines[1:]))
    return dict(command=command, response=response)


def generate(dir):
    for path in sorted(dir.iterdir()):
        if not path.is_dir() or path.name == '__pycache__':
            continue

        tests = [
            parse_test(f.read_text())
            for f in sorted(path.iterdir())
            if f.name.startswith(('test', 'example'))
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
    tests = [
        (test['command'], run_test(test['command']), test['response'])
        for test in test_batch['tests']
    ]
    server.terminate()

    for command, response, expected_response in tests:
        # print(command)
        assert response['status'] == expected_response['status']
        for header in expected_response['headers']:
            assert header in response['headers']
        if response['body_json']:
            assert response['body_json'] == expected_response['body_json']
        else:
            assert response['body'] == expected_response['body']
