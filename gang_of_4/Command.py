class Command:
    def execute(self):
        raise NotImplementedError


class Copy(Command):
    def execute(self):
        print("Copying ...")


class Paste(Command):
    def execute(self):
        print("Pasting ...")


class Save(Command):
    def execute(self):
        print("Saving ...")


class Macro:
    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def run(self):
        for command in self.commands:
            command.execute()


if __name__ == '__main__':
    macro = Macro()
    macro.add(Copy())
    macro.add(Paste())
    macro.add(Save())
    macro.run()
