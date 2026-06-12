from .command import Command

class InsertCommand(Command):
    def __init__(self, value):
        self.value = value
    
    def execute(self, editor):
        editor.history.append(editor.text)
        editor.text = f"{editor.text}{self.value}"