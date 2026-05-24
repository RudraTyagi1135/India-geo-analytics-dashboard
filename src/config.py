from pathlib import Path
from typing import Any

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = PROJECT_ROOT / "config.yaml"


def load_config(config_path: Path = CONFIG_PATH) -> dict[str, Any]:
    with config_path.open("r", encoding="utf-8") as config_file:
        config = yaml.safe_load(config_file)

    config["data"]["path"] = resolve_project_path(config["data"]["path"])
    return config


def resolve_project_path(path_value: str) -> Path:
    path = Path(path_value)
    if path.is_absolute():
        return path

    return PROJECT_ROOT / path
