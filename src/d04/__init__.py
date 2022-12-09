from utils import read_input
import re

if __name__ == '__main__':
    lines = read_input('sample.txt')
    lines = read_input('input-a.txt')
    re = re.compile('([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)')
    tot_1 = 0
    tot_2 = 0
    for l in lines:
        m = re.match(l)
        [i_0, i_1, j_0, j_1] = [int(m[1]), int(m[2]), int(m[3]), int(m[4])]
        if ((i_0 <= j_0) and (i_1 >= j_1)) or ((j_0 <= i_0) and (j_1 >= i_1)):
            tot_1 += 1
        if (i_1 < j_0)  or (j_1 < i_0):
            tot_2 += 1
    print(tot_1)
    print(len(lines) - tot_2)
