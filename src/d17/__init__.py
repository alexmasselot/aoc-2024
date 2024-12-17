from d17.computer import build_computer, Computer
from utils import read_input, read_input_blocks


def get_digit(c: Computer, dig: int, base: int):
    target = c.instructions[dig]
    ret = []
    for d in range(1, 8):
        a = base + (1 << (3 * dig)) * d
        c1 = c.copy()
        c1.registers[0] = a
        c1.operate_all()
        xs = [int(x) for x in c1.output().split(',')]
        if xs[dig] == target:
            ret.append(a)

    return ret


if __name__ == '__main__':
    blocks = read_input_blocks('input.txt')

    c = build_computer(blocks[0], blocks[1])
    print(c.instructions)

    def fhandler(b, dig):
        if dig == -1:
            return [b]

        bs = get_digit(c, dig, b)
        ret = []
        for b in bs:
            c1 = c.copy()
            c1.registers[0] = b
            c1.operate_all()
            ret.extend(fhandler(b, dig - 1))
        return ret
    sols = fhandler(0, 15)
    print(sols[0])