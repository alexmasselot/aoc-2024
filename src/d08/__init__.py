from utils import read_input

if __name__ == '__main__':
    lines = read_input('input-a.txt')
    n = len(lines)

    antennas = {}
    for r, l in enumerate(lines):
        for c, x in enumerate(l):
            if x != '.':
                if x not in antennas:
                    antennas[x] = []
                antennas[x].append((r, c))

    antinodes = set()
    for x, px in antennas.items():
        nx = len(px)
        for i in range(nx - 1):
            pi = px[i]
            for j in range(i + 1, nx):
                pj = px[j]
                v_r = (pj[0] - pi[0])
                v_c = (pj[1] - pi[1])
                r = pi[0] - v_r
                c = pi[1] - v_c
                if c >= 0 and c < n and r >= 0 and r < n:
                    antinodes.add((r, c))
                r = pj[0] + v_r
                c = pj[1] + v_c
                if c >= 0 and c < n and r >= 0 and r < n:
                    antinodes.add((r, c))
    print(len(antinodes))
    # part_2
    antinodes = set()
    for x, px in antennas.items():
        for a in px:
            antinodes.add(a)
        nx = len(px)
        for i in range(nx - 1):
            pi = px[i]
            for j in range(i + 1, nx):
                pj = px[j]
                v_r = (pj[0] - pi[0])
                v_c = (pj[1] - pi[1])
                r = pi[0] - v_r
                c = pi[1] - v_c
                while c >= 0 and c < n and r >= 0 and r < n:
                    antinodes.add((r, c))
                    r -= v_r
                    c -= v_c
                r = pj[0] + v_r
                c = pj[1] + v_c
                while c >= 0 and c < n and r >= 0 and r < n:
                    antinodes.add((r, c))
                    r += v_r
                    c += v_c
    print(len(antinodes))
