.PHONY: test fulltest
test:
	pipenv run python3 -m pytest --testmon tests

fulltest:
	pipenv run python3 -m pytest --random-order tests