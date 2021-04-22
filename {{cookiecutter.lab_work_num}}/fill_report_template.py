import re
from pathlib import Path

from docxtpl import DocxTemplate, InlineImage
from PIL import Image, ImageDraw, ImageFont


template = DocxTemplate(Path("template.docx"))
source_code = Path("{{cookiecutter.file_name}}.py").open().readlines()
test_results = Path("tests.txt").open().readlines()
meta = Path("metainfo.txt").open().readlines()

goal = re.search(
    r"(?<=Goal:\n)[\S\s]+(?=EndGoal)",
    "".join(meta),
).group(0)

summary = re.search(
    r"(?<=Summary:\n)[\S\s]+(?=EndSummary)",
    "".join(meta),
).group(0)

code = re.search(
    r"\"\"\"\n\n\n([\s\S]*)",
    "".join(source_code)
).group(1)

img = Image.new("RGB", (500, len(test_results) * 20), color="#232627")
canvas = ImageDraw.Draw(img)
font = ImageFont.truetype("font.ttf", size=9)
canvas.text((10, 10), "".join(test_results), font=font, fill="#FFFFFF")
img.save("tests.png")

context = {
    "number": "{{cookiecutter.lab_work_num}}",
    "subject": "{{cookiecutter.subject}}",
    "theme": "{{cookiecutter.theme}}",
    "author": "{{cookiecutter.author}}",
    "teacher": "{{cookiecutter.teacher}}",
    "year": "{{cookiecutter.year}}",
    "university": """{{cookiecutter.university}}""",
    "cathedra": "{{cookiecutter.cathedra}}",
    "group": "{{cookiecutter.group}}",
    "city": "{{cookiecutter.city}}",
    "goal": goal.strip(),
    "summary": summary.strip(),
    "source": code.strip(),
    "testing": InlineImage(template, "tests.png"),
}

template.render(context)
template.save(Path("report{{cookiecutter.lab_work_num}}.docx"))
