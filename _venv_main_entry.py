import importlib.util
import os
import sys
from pathlib import Path


def _load_legacy_main() -> object:
    # Загружаем файл pythonDIscordBot/.venv/main.py как модуль
    legacy_path = Path(__file__).resolve().parent / ".venv" / "main.py"
    spec = importlib.util.spec_from_file_location("_legacy_main", legacy_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Failed to create module spec for {legacy_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main():
    module = _load_legacy_main()
    # В legacy/main.py вызывается bot.run(...) на импорте, поэтому достаточно импорта.

