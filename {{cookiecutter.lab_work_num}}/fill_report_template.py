from pathlib import Path

from docxtpl import DocxTemplate


template = DocxTemplate(Path("report{{cookiecutter.lab_work_num}}.docx"))

context = {
    "subject": "{{cookiecutter.subject}}",
    "theme": "{{cookiecutter.theme}}",
}

template.render(context)
template.save(Path("report{{cookiecutter.lab_work_num}}.docx"))