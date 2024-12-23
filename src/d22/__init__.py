from utils import read_input


def next_secret(x):
    y = ((x << 6) ^ x) % 16777216
    z = ((y >> 5) ^ y) % 16777216
    return ((z * 2048) ^ z) % 16777216


def loop_secret(x, nb_steps):
    for _ in range(nb_steps):
        x = next_secret(x)
    return x


def list_secret(x, nb_steps):
    secrets = [x]
    for _ in range(nb_steps - 1):
        x = next_secret(x)
        secrets.append(x)
    return secrets


if __name__ == '__main__':
    xs = [int(l) for l in read_input('input.txt')]
    tot_1 = 0
    for x in xs:
        tot_1 += loop_secret(x, 2000)
    print(tot_1)

    prices = []
    deltas = []
    n = 2000
    tag_score = {}
    for x in xs:
        ps = [y % 10 for y in list_secret(x, n)]
        prices.append(ps)
        ds = [y - x for x, y in zip(ps, ps[1:])]
        ds = [str(x) if x >= 0 else chr(64 - x) for x in ds]
        ds = ''.join(ds)
        seen = set()
        for i in range(n - 5):
            seq = ds[i:(i + 4)]
            if seq in seen:
                continue
            seen.add(seq)
            if seq not in tag_score:
                tag_score[seq] = 0
            tag_score[seq] += ps[i + 4]
            # print(f'{seq}\t{ps[i+4]}')

    print(max(tag_score.values()))

# lines = read_input('input-a.txt')
