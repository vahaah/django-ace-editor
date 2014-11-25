update:
	DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

	git clone https://github.com/ajaxorg/ace-builds.git /tmp/ace
	cd  "${DIR}/djace_editor/static/djace_editor/ace"
	cp -R /tmp/ace/src/* ./

clean:
	@find . -name "*.pyc" -delete

release:
	@sed -ic -e s/`cat VERSION`/$(version)/ setup.py djace_editor/__init__.py
	@echo $(version) > VERSION
	@git add setup.py VERSION djace_editor/__init__.py
	@git commit -m "setup: bump to $(version)"
	@git tag $(version)
	@git push --tags
	@git push origin master
	@make clean
	@python setup.py sdist upload