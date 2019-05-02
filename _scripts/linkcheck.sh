#!/bin/bash
set -e

# Check external links
pipenv run sphinx-build -nW -b linkcheck en _build
pipenv run sphinx-build -nW -b linkcheck cs _build
