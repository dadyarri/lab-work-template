.PHONY: insert
insert:
	make tests
	python fill_report_template.py
ifeq ($(OS),Windows_NT)
	del /S tests.*
else
	rm -rf tests.*
endif


.PHONY: tests
tests:
ifeq ($(OS),Windows_NT)
	poetry run pytest tests
	poetry run pytest tests > tests.txt
else
	poetry run pytest tests | tee tests.txt
endif

