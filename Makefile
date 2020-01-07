install:
	python3 -m venv ./venv
	./venv/bin/pip install -r requirements.txt

build-en:
	./venv/bin/sphinx-build -nW -b html en _build

serve-en:
	./venv/bin/sphinx-autobuild en _build

build-cs:
	./venv/bin/sphinx-build -nW -b html cs _build

serve-cs:
	./venv/bin/sphinx-autobuild cs _build

# shortcuts for -cs
build: build-cs
serve: serve-cs

test:
	./venv/bin/pytest

linkcheck:
	./venv/bin/sphinx-build -nW -b linkcheck en _build
	./venv/bin/sphinx-build -nW -b linkcheck cs _build
