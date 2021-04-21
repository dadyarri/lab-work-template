import json
from pathlib import Path
import platform

if platform.system() == "Windows":
  print("Windows pre hook")
  config_path = Path("../cookiecutter.json")
  config = json.load(cookiecutter_config.open(encoding="UTF-8"))
  
  config_path.open("w", encoding="ANSI").write(json.dump(config))
