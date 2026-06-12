class Invoker:
    def execute_commands(self, commands, editor):
        for command in commands:
            command.execute(editor)