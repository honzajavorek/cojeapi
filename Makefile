build-en:
	sphinx-build -nW -b html en _build

serve-en:
	sphinx-autobuild en _build

build-cs:
	sphinx-build -nW -b html cs _build

serve-cs:
	sphinx-autobuild cs _build

# shortcuts for -cs
build: build-cs
serve: serve-cs

test:
	pytest

linkcheck:
	sphinx-build -nW -b linkcheck en _build
	sphinx-build -nW -b linkcheck cs _build
