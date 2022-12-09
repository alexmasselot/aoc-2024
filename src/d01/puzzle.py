filename = 'input-a.txt'

with open(filename) as fd:
    content = fd.read()

    loc_sums = list(map(lambda b: sum([int(l) for l in b.strip().split('\n')]), content.split('\n\n')))

    print(max(loc_sums))
    loc_sums.sort()
    print(sum(loc_sums[-3:]))
