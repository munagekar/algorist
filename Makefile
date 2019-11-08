.PHONY: test fulltest clean
test:
	pipenv run python3 -m pytest --testmon tests

fulltest:
	pipenv run python3 -m pytest --random-order tests

clean:
	find . -name '*.pyc' -delete
	find -name __pycache__ -delete
	rm -r .pytest_cache
	rm -r .testmondata