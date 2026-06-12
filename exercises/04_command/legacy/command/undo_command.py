from .command import Command

class UndoCommand(Command):
    def execute(self, editor):
        if editor.history:
            editor.text = editor.history.pop()