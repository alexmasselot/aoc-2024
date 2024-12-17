from d17.computer import build_computer
from utils import read_input, read_input_blocks

if __name__ == '__main__':
    blocks = read_input_blocks('sample.txt')

    c = build_computer(blocks[0], blocks[1])
    c.operate_all()
    print(c.output())
