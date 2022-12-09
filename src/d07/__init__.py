import re

from utils import read_input


def new_dir(name: str, parent=None):
    return {
        'name': name,
        'sub_dirs': [],
        'file_size': 0,
        'total_file_size': 0,
    }


def print_dir(d, depth=0):
    print('%s%s %s' % ((depth * ' '), d['file_size'], d['total_file_size']))
    for ds in d['sub_dirs']:
        print_dir(ds, depth + 1)


def sum_up_file_size(d):
    d['total_file_size'] = d['file_size']
    for ds in d['sub_dirs']:
        d['total_file_size'] += sum_up_file_size(ds)
    return d['total_file_size']


def walk_1(d, acc):
    if d['total_file_size'] <= 100000:
        acc.append(d['total_file_size'])
    for ds in d['sub_dirs']:
        walk_1(ds, acc)

def walk_2(d, best, target):
    if d['total_file_size'] > target:
        if d['total_file_size'] < best:
            best = d['total_file_size']
        l = [walk_2(ds, best, target) for ds in d['sub_dirs']]
        l.append(best)
        return min(l)
    return best


re_cd_fwd = re.compile('\$ cd (.+)')
re_file = re.compile('([0-9]+) .+')


def scan_dir(acc, lines, depth=0):
    if len(lines) == 0:
        return []

    while len(lines) != 0:
        l = lines[0]
        del lines[0]
        m_file = re_file.match(l)
        m_cd_fwd = re_cd_fwd.match(l)
        if m_file is not None:
            acc['file_size'] += int(m_file[1])
        elif l == '$ cd ..':
            return
        elif m_cd_fwd is not None:
            md = new_dir(m_cd_fwd[1], acc)
            acc['sub_dirs'].append(md)
            scan_dir(md, lines, depth + 1)
        else:
            print('WTF %s' % l)


if __name__ == '__main__':
    lines = [l for l in read_input('input-a.txt') if l != '$ ls' and not l.startswith('dir ')]

    root = new_dir('/')
    scan_dir(root, lines)
    sum_up_file_size(root)
    acc_1 = []
    walk_1(root, acc_1)
    print(sum(acc_1))

    need_to_free = root['total_file_size'] - 40000000
    b_2 = walk_2(root, 70000000, need_to_free)
    print(b_2)

