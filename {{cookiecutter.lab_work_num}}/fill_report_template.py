from pathlib import Path

from docxtpl import DocxTemplate


template = DocxTemplate(Path("report{{cookiecutter.lab_work_num}}.docx"))

context = {
    "number": "{{cookiecutter.lab_work_num}}",
    "subject": "{{cookiecutter.subject}}",
    "theme": "{{cookiecutter.theme}}",
    "author": "{{cookiecutter.author}}",
    "teacher": "{{cookiecutter.teacher}}",
    "year": "{{cookiecutter.year}}",
}

template.render(context)
template.save(Path("report{{cookiecutter.lab_work_num}}.docx"))