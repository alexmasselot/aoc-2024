from utils import read_input_blocks

memoize = {}


class Computer2:
    instructions: list[str]

    def __init__(self, instructions: list[int]):
        self.instructions = [*instructions]
        self.nb_instructions = len(instructions)


    def key(self, registers: list[int], idx: int):
        return f'''{registers}/{self.instructions}/{idx}'''

    def combo(self, operand: int, registers: list[int]) -> int:
        if operand <= 3:
            return operand
        if operand == 7:
            return None
        return registers[operand - 4]

    def operate(self, idx: int, registers: list[int]) -> tuple[int, list[int], int | None]:
        opcode = self.instructions[idx]
        operand = self.instructions[idx + 1]
        out_reg = [*registers]
        c = self.combo(operand, out_reg)
        if opcode == 0:
            out_reg[0] = int(registers[0] / (1 << c))
            return idx + 2, out_reg, None

        if opcode == 1:
            out_reg[1] = registers[1] ^ operand
            return idx + 2, out_reg, None

        if opcode == 2:
            out_reg[1] = c % 8
            return idx + 2, out_reg, None

        if opcode == 3:
            if registers[0] == 0:
                return idx + 2, out_reg, None
            return operand, out_reg, None

        if opcode == 4:
            out_reg[1] = registers[1] ^ registers[2]
            return idx + 2, out_reg, None

        if opcode == 5:
            return idx + 2, out_reg, c % 8

        if opcode == 6:
            out_reg[1] = int(registers[0] / (1 << c))
            return idx + 2, out_reg, None

        if opcode == 7:
            out_reg[2] = int(registers[0] / (1 << c))
            return idx + 2, out_reg, None

    def operate_all(self, registers: list[int]):
        def fhandler(idx, registers: list[int], acc: str | None) -> tuple[int, list[int], str | None]:
            if idx >= self.nb_instructions:
                return idx, registers, acc
            k = self.key(registers, idx)
            if k in memoize:
                i, regs, m = memoize[k]
                if acc is None:
                    return i, regs, m
                if m is None:
                    return i, regs, acc
                return i, regs, acc + ',' + m
            i, regs, m = self.operate(idx, registers)
            if acc is None and m is not None:
                acc_n = str(m)
            elif m is None:
                acc_n = acc
            else:
                acc_n = acc + ',' + str(m)
            memoize[k] = fhandler(i, regs, acc_n)
            return memoize[k]

        _, _, o = fhandler(0, registers, None)
        return o


#                if not output_match.startswith(self.out):
#                    return None


def operate_until(computer: Computer2, registers: list[int]):
    match_output = ','.join([str(x) for x in computer.instructions])
    for a in range(10000000000000):
    # for a in range(117440, 117441):
        regs = [*registers]
        regs[0] = a
        if a % 100000 == 0:
            print(a)
        c = computer.operate_all(regs)
        if c is not None and c == match_output:
            print(f'WINNER {a}')
            print(c)
            return c


def build_computer2(inp_reg: str = None, input_instructions: str = None) -> tuple[Computer2, list[int]]:
    if input is None:
        return Computer2([]), [0 for _ in range(3)]
    registers = [int(x.split(': ')[1]) for x in inp_reg.split('\n')]
    instructions = [int(x) for x in input_instructions.split(': ')[1].split(',')]
    memoize.clear()
    return Computer2(instructions), registers


if __name__ == '__main__':
    blocks = read_input_blocks('input.txt')

    c, registers = build_computer2(blocks[0], blocks[1])
    o = operate_until(c, registers)

