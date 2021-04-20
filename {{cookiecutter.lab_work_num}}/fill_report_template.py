import re
from pathlib import Path

from docxtpl import DocxTemplate


template = DocxTemplate(Path("report{{cookiecutter.lab_work_num}}.docx"))
source_code = Path("{{cookiecutter.file_name}}.py").open().readlines()

goal = re.search(
    r"(?<=\"\"\"\nGoal:\n)[\S\s]+(?=EndGoal)",
    "".join(source_code),
).group(0)

summary = re.search(
    r"(?<=Summary:\n)[\S\s]+(?=EndSummary\n\"\"\")",
    "".join(source_code),
).group(0)

code = re.search(
    r"\"\"\"\n\n\n([\s\S]*)",
    "".join(source_code)
).group(1)

context = {
    "number": "{{cookiecutter.lab_work_num}}",
    "subject": "{{cookiecutter.subject}}",
    "theme": "{{cookiecutter.theme}}",
    "author": "{{cookiecutter.author}}",
    "teacher": "{{cookiecutter.teacher}}",
    "year": "{{cookiecutter.year}}",
    "goal": goal.strip(),
    "summary": summary.strip(),
    "source": code.strip()
}

template.render(context)
template.save(Path("report{{cookiecutter.lab_work_num}}.docx"))