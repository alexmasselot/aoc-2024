from utils import read_input


def check_pair_invalid(x1, x2):
    return x2 <= x1 or x2 > (x1 + 3)


def check_increase(xs: list[int], allow_skip=0):
    skipped = 0
    x = xs[0]
    for i, x1 in enumerate(xs[1:]):
        if check_pair_invalid(x, x1):
            if skipped >= allow_skip:
                return False
            skipped += 1
            if i == 0:
                if check_pair_invalid(xs[0], xs[2]):
                    x = xs[1]
            continue
        x = x1
    return True


def check_decrease(xs: list[int], allow_skip=0):
    xs = [*xs]
    xs.reverse()
    return check_increase(xs, allow_skip)


if __name__ == '__main__':
    lines = read_input('input-a.txt')
    lines = [list(map(int, line.strip().split())) for line in lines]
    n_1 = 0
    n_2 = 0
    for l in lines:
        if check_decrease(l) or check_increase(l):
            n_1 += 1
        if check_decrease(l, 1) or check_increase(l, 1):
            n_2 += 1
    print(n_1)
    print(n_2)
