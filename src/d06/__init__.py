from utils import read_input


def marker_1(str, n):
    for i in range(0, len(str) - n):
        b = str[i:(i + n)]
        if len(set(list(b))) == n:
            return i + n


if __name__ == '__main__':
    lines = read_input('input-a.txt')
    print(marker_1(lines[0], 4))
    print(marker_1(lines[0], 14))
