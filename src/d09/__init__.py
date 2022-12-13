import numpy as np

from utils import read_input


def tail_new_pos(t, h):
    v = (h[0] - t[0], h[1] - t[1])
    if max(abs(v[0]), abs(v[1])) < 2:
        return t
    # in fact, distance v is never greater than 2
    m_0 = int(v[0] / abs(v[0])) if abs(v[0]) >= 2 else v[0]
    m_1 = int(v[1] / abs(v[1])) if abs(v[1]) >= 2 else v[1]
    return t[0] + m_0, t[1] + m_1


def move_head(h, d):
    if d == 'U':
        return h[0], h[1] + 1
    if d == 'D':
        return h[0], h[1] - 1
    if d == 'R':
        return h[0] + 1, h[1]
    if d == 'L':
        return h[0] - 1, h[1]


def next_move_stack(move_stack):
    '''

    :param move_stack: the list of move to make
    :type move_stack: list[tuple[str, int]]
    :return: a tuple with direction and the remaining move. Eventually None ofr direction if the move are completed
    :rtype:
    '''
    if len(move_stack) == 0:
        return None, []
    move = move_stack[0]
    if move[1] == 1:
        new_stack = move_stack[1:]
    else:
        new_stack = [(move[0], move[1] - 1)] + move_stack[1:]
    return move[0], new_stack


def move_it(move_stack):
    head = (0, 0)
    tail = (0, 0)
    visited = set()
    d, next_moves = next_move_stack(move_stack)
    while d is not None:
        head = move_head(head, d)
        tail = tail_new_pos(tail, head)
        visited.add(tail)
        d, next_moves = next_move_stack(next_moves)
    return visited


def print_string(string):
    x_min = -15
    x_max = 15
    y_min = -18
    y_max = 10

    mat = np.full([x_max - x_min + 1, y_max - y_min + 1], '.', dtype=str)
    for i in range(0, len(string)):
        p = string[i]
        x = x_max - p[1]
        y = p[0] + y_min
        if mat[x, y] == '.':
            mat[x, y] = str(i)

    s = np.array2string(mat, separator='', max_line_width=160)
    s = s.replace("'", '').replace('[', '').replace(']', '')
    print(s)


def move_it_9(move_stack):
    string = [(0, 0) for i in range(0, 10)]
    visited = set()
    prev_d = None
    d, next_moves = next_move_stack(move_stack)
    while d is not None:
        string[0] = move_head(string[0], d)
        for i in range(1, 10):
            string[i] = tail_new_pos(string[i], string[i - 1])
        visited.add(string[9])
        # print(next_moves)
        d, next_moves = next_move_stack(next_moves)
        # if prev_d is not d:
        #    print_string(string)
        prev_d = d
    return visited


if __name__ == '__main__':
    lines = read_input('input-a.txt')
    moves = [(t[0], int(t[1])) for t in [l.split(' ') for l in lines]]
    visited = move_it(moves)
    print(len(visited))

    visited_2 = move_it_9(moves)
    print(len(visited_2))
