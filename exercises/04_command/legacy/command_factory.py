from command.insert_command import InsertCommand
from command.delete_command import DeleteCommand
from command.replace_command import ReplaceCommand
from command.undo_command import UndoCommand

class CommandFactory:
    def choose_command(self, command, value):
        match(command):
            case 'insert':
                return InsertCommand(value)
            case 'delete':
                return DeleteCommand(value)
            case 'replace':
                return ReplaceCommand(value)
            case 'undo':
                return UndoCommand()
            case _:
                raise Exception('Invalid command')