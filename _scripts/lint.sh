#!/bin/bash
set -e

# Make sure requirements.txt are in sync with Pipfile.lock
pipenv run pipenv_to_requirements -f -o ci-requirements.txt
if ! diff requirements.txt ci-requirements.txt > /dev/null
then
  help_url='https://cojeapi.readthedocs.io/cs/latest/CONTRIBUTING.html#zavislosti'
  echo ""
  echo ""
  echo "The requirements.txt file is not up to date. Run" \
    "'pipenv run requirements' and commit the changes." \
    "See ${help_url} for more info."
  exit 1
fi

# doc8
doc8

# Check external links
pipenv run sphinx-build -nW -b linkcheck . _build
