from d15.grid import Grid
from d15.grid2 import Grid2, build_grid2
from utils import read_input_blocks

c_dir = {
    '^': 0,
    '>': 1,
    'v': 2,
    '<': 3,
}


def read_move_sequence(input: str):
    return [c_dir[c] for c in input.replace('\n', '')]


if __name__ == '__main__':
    blocks = read_input_blocks('input.txt')

    grid = Grid(blocks[0])
    move_sequence = read_move_sequence(blocks[1])

    for move in move_sequence:
        grid.move(move)

    print(grid.coords_sum())

    grid2 = build_grid2(blocks[0])
    for move in move_sequence:
        grid2.move(move)
        # print (f'-------------- {move}')
        # print(grid2)

    print(grid2.coords_sum())
