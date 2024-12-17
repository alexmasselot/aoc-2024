from utils import read_input, read_input_blocks

memoize = {}

class Computer:
    registers: list[int]
    instructions: list[str]
    out: str

    def __init__(self, registers: list[int], instructions: list[int]):
        self.registers = [*registers]
        self.instructions = [*instructions]
        self.out = None

    def __str__(self):
        return f'{self.registers} {self.instructions} {self.out}'

    def copy(self):
        return Computer(self.registers, self.instructions)

    def output(self):
        if self.out is None:
            return ''
        return self.out

    def key(self, idx: int):
        return f'''{self.registers}/{self.instructions}/{idx}'''

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
            if self.out is None:
                self.out = str(c % 8)
            else:
                self.out += ',' + str(c % 8)
            return idx + 2

        if opcode == 6:
            self.registers[1] = int(self.registers[0] / (1 << c))
            return idx + 2

        if opcode == 7:
            self.registers[2] = int(self.registers[0] / (1 << c))
            return idx + 2

    def operate_all(self, output_match: str = None):

        idx = 0
        while idx < len(self.instructions):
            print(f'idx={idx}')
            k = self.key(idx)
            if k in memoize:
                print(f'MEMO {k} {memoize[k]}')
                i, regs, m = memoize[k]
                if self.out is None:
                    self.out = m
                elif m is not None:
                    self.out = self.out + ',' + m
                self.registers = regs
                idx = i
            else:
                idx = self.operate(idx)
                memoize[k] = (idx, [*self.registers], self.out)
                print(f'saving {k}-> {memoize[k]}')
            # print(idx)
            if output_match is not None and self.out is not None:
                print(f'{output_match}//{self.out} ')
                if output_match == self.out:
                    return self
#                if not output_match.startswith(self.out):
#                    return None


def operate_until(computer: Computer):
    match_output = ','.join([str(x) for x in computer.instructions])
    # for a in range(10000000000000):
    for a in range(117440,117441):
        print(f'---------------- {a}')
        computer_a = computer.copy()
        computer_a.registers[0] = a
        computer_anchor = computer_a.copy()
        if a % 100000 == 0:
            print(a)
        print(computer_anchor)
        c = computer_anchor.operate_all(match_output)
        if c is not None:
            print(f'WINNER {a}')
            print(c.registers)
            break


def build_computer(inp_reg: str = None, input_instructions: str = None):
    if input is None:
        return Computer([0 for _ in range(3)], [])
    registers = [int(x.split(': ')[1]) for x in inp_reg.split('\n')]
    instructions = [int(x) for x in input_instructions.split(': ')[1].split(',')]
    memoize.clear()
    return Computer(registers, instructions)


if __name__ == '__main__':
    blocks = read_input_blocks('sample-1.txt')

    # c = build_computer(blocks[0], blocks[1])
    # c.operate_all()
    # print(c.output())

    c = build_computer(blocks[0], blocks[1])
    operate_until(c)
