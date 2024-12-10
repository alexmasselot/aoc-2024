import re

from utils import read_input

if __name__ == '__main__':
    text = ''.join(read_input('input-a.txt'))
    pat = r'''mul\(([0-9]+),([0-9]+)\)'''
    tot_1 = 0
    for m in re.findall(pat, text):
        i1, i2 = m
        tot_1 += int(i1) * int(i2)
    print(tot_1)

    text = f"do(){text}don't()"
    pat_do = r'''do\(\).*?don't\(\)'''
    tot_2 = 0
    for m_do in re.findall(pat_do, text):
        for m in re.findall(pat, m_do):
            i1, i2 = m
            tot_2 += int(i1) * int(i2)
    print(tot_2)
