from utils import read_input, read_input_blocks


def read_key_lock(input: str):
    ls = [list(l) for l in input.split('\n')]
    transposed = list(zip(*ls))
    if transposed[0][0] == '#':
        return True, [l.index('.') - 1 for l in transposed]
    else:
        return False, [6 - l.index('#') for l in transposed]


def read_key_locks(blocks: list[str]):
    ls = []
    ks = []
    for b in blocks:
        is_lock, vs = read_key_lock(b)
        if is_lock:
            ls.append(vs)
        else:
            ks.append(vs)
    return ls, ks


if __name__ == '__main__':
    locks, keys = read_key_locks(read_input_blocks('input.txt'))

    tot_1 = 0
    for l in locks:
        print(f'l={l}')
        for k in keys:
            if all(l[i]+k[i]<=5 for i in range(5)):
                tot_1 += 1

    print(tot_1)