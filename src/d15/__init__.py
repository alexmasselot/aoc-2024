import re
from sympy import Interval, Union
from tqdm import tqdm


from utils import read_input

# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
re_read_line = re.compile(
    'Sensor at x=(\\-?[0-9]+), y=(\\-?[0-9]+): closest beacon is at x=(\\-?[0-9]+), y=(\\-?[0-9]+)')


def dist(p):
    ((x1, y1), (x2, y2)) = p
    return abs(x1 - x2) + abs(y1 - y2)


def sensor_beacon_y_coverage(sb, y):
    ((xs, ys), (xb, yb)) = sb
    d = dist(sb)
    if abs(y - ys) > d:
        return None
    return xs - d + abs(y - ys), xs + d - abs(y - ys)


def interval_union(intervals):
    intervals = [Interval(begin - 0.5, end + 0.5) for (begin, end) in intervals]
    return Union(*intervals)


def read_line(text: str):
    m = re_read_line.match(text)
    return (int(m[1]), int(m[2])), (int(m[3]), int(m[4]))


if __name__ == '__main__':
    is_part_1 = False
    if is_part_1:
        y_1 = 10
        xy_max = 20
        filename = 'sample.txt'
    else:
        y_1 = 2000000
        xy_max = 4000000
        filename = 'input-a.txt'

    lines = read_input(filename)
    sensor_beacons = [read_line(l) for l in lines]
    intervs = [sensor_beacon_y_coverage(sb, y_1) for sb in sensor_beacons]
    intervs = [i for i in intervs if i is not None]

    print(interval_union(intervs).measure)

    for y in tqdm(range(xy_max)):
        intervs = [sensor_beacon_y_coverage(sb, y) for sb in sensor_beacons]
        intervs = [i for i in intervs if i is not None]
        intervs = interval_union(intervs).intersection(Interval(0, xy_max))
        if type(intervs) == Union:
            x = int((intervs.args[0].end + intervs.args[1].start) / 2)
            print('%d\t%d\t%d' % (x, y, x * 4000000 + y))
