from .command import Command

class ReplaceCommand(Command):
    def __init__(self, value):
        self.value = value
        
    def execute(self, editor):
        editor.history.append(editor.text)
        old, new = self.value
        editor.text = editor.text.replace(old, new, 1)