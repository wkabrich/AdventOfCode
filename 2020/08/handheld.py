
# class for the handheld game console

class Handheld:

    def __init__(self, instructions):
        self.accumulator = 0
        self.instructions = instructions
        self.index = 0

    def process(self):
        instruction = self.instructions[self.index].split(' ')

        self.funcMapping.get(instruction[0])(self=self, value=instruction[1])

    def processinstruction(self, instruction):
        self.funcMapping.get(instruction[0])(self=self, value=instruction[1])

    def nop(self, value):
        self.index += 1

    def acc(self, value):
        self.accumulator += int(value)
        self.index += 1

    def jmp(self, value):
        self.index += int(value)

    funcMapping = {
        'nop': nop,
        'acc': acc,
        'jmp': jmp
    }
