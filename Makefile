default: develop

develop: 
	jekyll serve --livereload

build: install
	jekyll build
