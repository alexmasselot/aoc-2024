import functools
import re

from utils import read_input, read_input_blocks


def match_1(text: str, patterns: list[str]) -> int:
    memoize = {}

    @functools.cache
    def fhandler(rem: str) -> int:
        return sum(fhandler(rem[len(p):]) for p in patterns if rem.startswith(p)) if rem else 1

    return fhandler(text)


if __name__ == '__main__':
    blocks = read_input_blocks('input.txt')

    patterns = blocks[0].split(', ')
    targets = blocks[1].split('\n')

    # rx = fr'''(?:{'|'.join(patterns)}|{'|'.join([p[::-1] for p in patterns])})+'''
    rx = fr'''({'|'.join(patterns)})+'''
    print(rx)

    tot_1 = 0
    tot_2 = 0
    for t in targets:
        # m = re.fullmatch(rx, t)
        # print(f'{m is not None}\t{t}')
        # if m is not None:
        #     tot_1 += 1
        m = match_1(t, patterns)
        if m>0:
            tot_1 += 1
        tot_2 += m

    # 400 is too high
    print(tot_1)
    print(tot_2)

    # lines = read_input('input-a.txt')
