.PHONY: insert
insert:
	python fill_report_template.py
	ifeq ($(OS), Windows_NT)
		del /S tests.*
	else
		rm -rf tests.*
	endif

.PHONY: tests
tests:
	poetry run pytest tests > tests.txt
