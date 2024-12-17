from utils import read_input, read_input_blocks


class Computer:
    registers: list[int]
    instructions: list[str]
    out: list[int]

    def __init__(self, registers: list[int], instructions: list[int]):
        self.registers = [*registers]
        self.instructions = [*instructions]
        self.out = []

    def output(self):
        return ','.join([str(x) for x in self.out])

    def combo(self, operand: int) -> int:
        if operand <= 3:
            return operand
        if operand == 7:
            return None
        return self.registers[operand - 4]

    def operate(self, idx: int) -> int:
        opcode = self.instructions[idx]
        operand = self.instructions[idx + 1]
        c = self.combo(operand)
        if opcode == 0:
            self.registers[0] = int(self.registers[0] / (1 << c))
            return idx + 2

        if opcode == 1:
            self.registers[1] = self.registers[1] ^ operand
            return idx + 2

        if opcode == 2:
            self.registers[1] = c % 8
            return idx + 2

        if opcode == 3:
            if self.registers[0] == 0:
                return idx + 2
            return operand

        if opcode == 4:
            self.registers[1] = self.registers[1] ^ self.registers[2]
            return idx + 2

        if opcode == 5:
            self.out.append(c % 8)
            return idx + 2

        if opcode == 6:
            self.registers[1] = int(self.registers[0] / (1 << c))
            return idx + 2

        if opcode == 7:
            self.registers[2] = int(self.registers[0] / (1 << c))
            return idx + 2

    def operate_all(self):
        idx = 0
        while idx < len(self.instructions):
            idx = self.operate(idx)


def build_computer(inp_reg: str = None, input_instructions: str = None):
    if input is None:
        return Computer([0 for _ in range(3)], [])
    registers = [int(x.split(': ')[1]) for x in inp_reg.split('\n')]
    instructions = [int(x) for x in input_instructions.split(': ')[1].split(',')]
    return Computer(registers, instructions)


if __name__ == '__main__':
    blocks = read_input_blocks('input.txt')

    c = build_computer(blocks[0], blocks[1])
    c.operate_all()
    print(c.output())
    # lines = read_input('input-a.txt')
