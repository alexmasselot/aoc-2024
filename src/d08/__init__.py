from utils import read_input, np_dense_matrix

import numpy as np

if __name__ == '__main__':
    mat = np_dense_matrix('input-a.txt')
    n = mat.shape[0]

    from_w = mat.copy()
    from_w.fill(-1)

    from_e = mat.copy()
    from_e.fill(-1)

    from_n = mat.copy()
    from_n.fill(-1)

    from_s = mat.copy()
    from_s.fill(-1)

    for i in range(1, n - 1):
        from_w[:, i] = np.maximum(from_w[:, i - 1], mat[:, i - 1])
        from_e[:, n - i - 1] = np.maximum(from_e[:, n - i], mat[:, n - i])
        from_n[i, :] = np.maximum(from_n[i - 1, :], mat[i - 1, :])
        from_s[n - i - 1, :] = np.maximum(from_s[n - i, :], mat[n - i, :])
    from_min = np.minimum(from_w, np.minimum(from_e, np.minimum(from_s, from_n)))
    print(np.greater(mat, from_min).sum())

    print(mat)
    view_map = mat.copy()
    view_map.fill(1)
    for i in range(0,n):
        for j in range(0,n):
            t = mat[i, j]

            view = 0
            x = j - 1
            while x >= 0 and mat[i, x] < t:
                view += 1
                x = x - 1
            if x > 0:
                view += 1
            view_map[i, j] = view_map[i, j] * view

            view = 0
            x = j + 1
            while x < n and mat[i, x] < t:
                view += 1
                x = x + 1
            if x < n:
                view += 1
            view_map[i, j] = view_map[i, j] * view

            view = 0
            x = i - 1
            while x >= 0 and mat[x, j] < t:
                view += 1
                x = x - 1
            if x > 0:
                view += 1
            view_map[i, j] = view_map[i, j] * view

            view = 0
            x = i + 1
            while x < n and mat[x, j] < t:
                view += 1
                x = x + 1
            if x < n:
                view += 1
            view_map[i, j] = view_map[i, j] * view
    print(view_map.max())
