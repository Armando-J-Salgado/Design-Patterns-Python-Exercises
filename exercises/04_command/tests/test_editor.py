from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "legacy"))

from editor import Editor


def test_editor_executes_actions_and_undoes_last_change():
    editor = Editor()

    assert editor.execute("insert", "hello") == "hello"
    assert editor.execute("insert", " world") == "hello world"
    assert editor.execute("replace", ("world", "team")) == "hello team"
    assert editor.execute("undo") == "hello world"
    assert editor.execute("delete", 6) == "hello"
    assert editor.execute("undo") == "hello world"
