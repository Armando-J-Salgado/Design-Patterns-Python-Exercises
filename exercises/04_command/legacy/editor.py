from command.invoker import Invoker
from command_factory import CommandFactory
class Editor:
    def __init__(self):
        self.text = ""
        self.history = []

    def execute(self, action, value=None):
        command = CommandFactory().choose_command(action, value)
        Invoker().execute_commands([command], self)
        return self.text


        
