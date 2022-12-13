import re

from utils import read_input

if __name__ == '__main__':
    lines = read_input('input-a.txt')
    # lines = read_input('input-a.txt')

    v = 1
    re_addx = re.compile('addx (\-?[0-9]+)')
    add_x = 1
    time_value = [0, add_x]
    for l in lines:
        m = re_addx.match(l)
        if m is not None:
            time_value.append(add_x)
            add_x += int(m[1])
            time_value.append(add_x)
        else:
            time_value.append(add_x)

    tot = 0
    i = 20
    while i < len(time_value):
        tot += time_value[i] * i
        i += 40
    print(tot)

    raster = ['.' for i in range(0, 240)]
    for i in range(1, len(time_value)):
        if abs((i - 1) % 40 - time_value[i]) <= 1:
            raster[i-1] = '#'

    for r in range(0, 6):
        print(''.join(raster[(r * 40):((r + 1) * 40 )]))
