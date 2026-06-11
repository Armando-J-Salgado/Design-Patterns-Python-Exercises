from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "legacy"))

import settings as settings_module
from settings import AppSettings, settings


def test_single_instance_is_shared():
    AppSettings._instance = None
    first = settings()
    second = settings()

    assert first is second


def test_state_is_shared_between_references():
    AppSettings._instance = None
    first = settings()
    second = settings()

    first.set("theme", "dark")
    assert second.get("theme") == "dark"
    assert settings_module.settings().get("theme") == "dark"
