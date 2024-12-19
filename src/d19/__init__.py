import re

from utils import read_input, read_input_blocks


def match_1(text: str, patterns: list[str]):
    memoize = {}

    def fhandler(rem: str, patterns: list[str]) -> bool:
        nonlocal memoize
        if rem in memoize:
            return memoize[rem]
        if rem == '':
            return True
        any_match = False
        for p in patterns:
            if rem.startswith(p):
                any_match = any_match or fhandler(rem[len(p):], patterns)
        memoize[rem] = any_match
        return any_match

    return fhandler(text, patterns)


if __name__ == '__main__':
    blocks = read_input_blocks('input.txt')

    patterns = blocks[0].split(', ')
    targets = blocks[1].split('\n')

    # rx = fr'''(?:{'|'.join(patterns)}|{'|'.join([p[::-1] for p in patterns])})+'''
    rx = fr'''({'|'.join(patterns)})+'''
    print(rx)

    tot_1 = 0
    for t in targets:
        # m = re.fullmatch(rx, t)
        # print(f'{m is not None}\t{t}')
        # if m is not None:
        #     tot_1 += 1
        m = match_1(t, patterns)
        print(f'{m}\t{t}')
        if m:
            tot_1 += 1

    # 400 is too high
    print(tot_1)

    # lines = read_input('input-a.txt')
