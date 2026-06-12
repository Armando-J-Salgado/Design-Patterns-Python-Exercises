from .command import Command

class DeleteCommand(Command):
    def __init__(self, value):
        self.value = value
    
    def execute(self, editor):
        editor.history.append(editor.text)
        count = int(self.value or 0)
        editor.text = editor.text[:-count] if count else editor.text