def read_input(filename: str):
    with open(filename) as fd:
        return [l.replace('\n', '') for l in fd.readlines()]
