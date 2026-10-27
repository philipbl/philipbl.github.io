CV_DIR ?= ../cv
PYTHON ?= $(CV_DIR)/.venv/bin/python

# Always rebuild: it takes under a second, and checkout mtimes can't be trusted.
build:
	$(MAKE) -C $(CV_DIR)
	cp $(CV_DIR)/cv.pdf docs/lundrigan-cv.pdf
	$(PYTHON) build.py $(CV_DIR)/cv_data.yml

test:
	$(PYTHON) -m doctest build.py

serve: build
	python3 -m http.server 8000

.PHONY: build test serve
