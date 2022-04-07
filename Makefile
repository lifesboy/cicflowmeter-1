VERSION:=$(shell python3 setup.py --version)

install:
	python3 setup.py install

uninstall:
	pip3 uninstall cicflowmeter -y

clean:
	rm -rf *.egg-info build dist report.xml

build:
	python3 setup.py sdist bdist_wheel --universal

release:
	@git tag -a v$(VERSION)
	@git push --tag
