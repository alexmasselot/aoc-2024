import numpy as np

from utils import read_input

if __name__ == '__main__':
    lines = read_input('input-a.txt')
    # lines = read_input('input-a.txt')

    chars = [r for r in [
        list(l) for l in lines
    ]]

    heights = np.array(chars)
    start = np.where(heights == 'S')
    end = np.where(heights == 'E')
    start = (start[0][0], start[1][0])
    end = (end[0][0], end[1][0])
    heights[start[0]][start[1]] = 'a'
    heights[end[0]][end[1]] = 'z'
    applyall = np.vectorize(lambda c: ord(c) - ord('a'))
    heights = applyall(heights)

    move_from_n = heights <= (np.roll(heights, 1, axis=0) + 1)
    move_from_n[0, :] = False
    move_from_s = heights <= (np.roll(heights, -1, axis=0) + 1)
    move_from_s[-1, :] = False
    move_from_e = heights <= (np.roll(heights, -1, axis=1) + 1)
    move_from_e[:, -1] = False
    move_from_w = heights <= (np.roll(heights, 1, axis=1) + 1)
    move_from_w[:, 0] = False


    def walk_from(x, y):
        steps_to_here = np.full(heights.shape, fill_value=999999)
        steps_to_here[x, y] = 0

        new_steps = None
        while np.any(steps_to_here != new_steps):
            if new_steps is None:
                new_steps = steps_to_here
            steps_to_here = new_steps
            d = np.roll(steps_to_here, 1, axis=0) + 1
            new_steps = np.where(np.logical_and(move_from_n, d < steps_to_here), d, steps_to_here)
            d = np.roll(steps_to_here, -1, axis=0) + 1
            new_steps = np.where(np.logical_and(move_from_s, d < new_steps), d, new_steps)
            d = np.roll(steps_to_here, -1, axis=1) + 1
            new_steps = np.where(np.logical_and(move_from_e, d < new_steps), d, new_steps)
            d = np.roll(steps_to_here, 1, axis=1) + 1
            new_steps = np.where(np.logical_and(move_from_w, d < new_steps), d, new_steps)

        return steps_to_here[end[0], end[1]]


    # part 1
    print(walk_from(start[0], start[1]))

    (xs, ys) = np.where(heights == 0)
    dist = []
    for i in range(0, len(xs)):
        dist.append(walk_from(xs[i], ys[i]))
    print(min(dist))
