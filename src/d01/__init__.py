from utils import read_input

if __name__ == '__main__':
    lines = read_input('input-a.txt')
    xs = [list(map(int, l.split('   '))) for l in lines]
    xs1, xs2 = zip(*xs)
    xs1=list(xs1)
    xs2=list(xs2)
    xs1.sort()
    xs2.sort()
    n = 0
    for x1, x2 in zip(xs1, xs2):
        n += abs(x1- x2)
    print(n)

    n_2=0
    for x1 in xs1:
        n_2 += x1*xs2.count(x1)
    print(n_2)
    # lines = read_input('input-a.txt')
