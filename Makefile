css:
	docker run --rm -v `pwd`:/sass -w /sass kvikshaug/sass sass -t compressed --scss --no-cache --update style.scss:style.css

css-watch:
	docker run --rm -v `pwd`:/sass -w /sass kvikshaug/sass sass -t compressed --scss --no-cache --watch style.scss:style.css
