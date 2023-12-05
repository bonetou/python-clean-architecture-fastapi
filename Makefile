run-all-tests:
	poetry run pytest tests/ -vv

check-tests-coverage:
	poetry run pytest --cov=book_store --cov-report=html --cov-report=term --cov-fail-under=95
