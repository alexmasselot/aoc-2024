from utils import read_input


def blink_stone(i: int) -> list[int]:
    if i == 0:
        return [1]
    s = str(i)
    n = len(s)

    if n % 2 == 0:
        n_mid = n >> 1
        return [int(s[:n_mid]), int(s[n_mid:])]

    return [i * 2024]


memoize = {}


def blink_rec(i: int, rem_steps: int):
    if rem_steps == 0:
        return 1, [i]
    key = f'{i}/{rem_steps}'
    if key in memoize:
        return memoize[key], None
    vs = blink_stone(i)
    ret = []
    tot = 0
    for v in vs:
        n, xs = blink_rec(v, rem_steps - 1)
        tot += n
        if xs is not None:
            ret = ret + xs
    memoize[key] = tot
    return tot, ret


def blink_stones(vals: list[int], steps: int) -> int:
    tot = 0
    for v in vals:
        n, _ = blink_rec(v, steps)
        tot += n
    return tot


if __name__ == '__main__':
    input = list(map(int, read_input('input-a.txt')[0].split(' ')))
    stones = [*input]
    n = blink_stones(stones, 75)
    print(n)
# lines = read_input('input-a.txt')
