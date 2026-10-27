CV_DIR ?= ../cv
PYTHON ?= $(CV_DIR)/.venv/bin/python
SITE = _site

# Build the CV PDF and the page into $(SITE)/. CI runs this on every push;
# run it locally to preview. Always rebuilds: it takes seconds.
build:
	$(MAKE) -C $(CV_DIR)
	rm -rf $(SITE)
	mkdir -p $(SITE)
	cp -R css images docs $(SITE)/
	cp $(CV_DIR)/cv.pdf $(SITE)/docs/lundrigan-cv.pdf
	$(PYTHON) build.py $(CV_DIR)/cv_data.yml $(SITE)/index.html

# Needs lychee locally: brew install lychee
test: build
	$(PYTHON) -m doctest build.py
	lychee --offline --no-progress '$(SITE)/**/*.html'

serve: build
	python3 -m http.server -d $(SITE) 8000

.PHONY: build test serve
