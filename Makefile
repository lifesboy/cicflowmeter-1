VERSION:=$(shell python3 setup.py --version)

install:
    #python3 setup.py install
	python3 -m pip install importlib-metadata==4.8.1
	python3 setup.py bdist_wheel
	python3 -m pip install dist/cicflowmeter-0.1.7-py3-none-any.whl

uninstall:
	pip3 uninstall cicflowmeter -y

clean:
	rm -rf *.egg-info build dist report.xml

build:
	python3 setup.py sdist bdist_wheel --universal

release:
	@git tag -a v$(VERSION)
	@git push --tag
