.PHONY: insert
insert:
	python fill_report_template.py
	rm -rf tests.*

.PHONY: tests
tests:
	poetry run pytest tests > tests.txt
	echo "ok"