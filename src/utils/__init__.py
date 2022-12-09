def read_input(filename: str):
    with open(filename) as fd:
        return [l.strip() for l in fd.readlines()]
