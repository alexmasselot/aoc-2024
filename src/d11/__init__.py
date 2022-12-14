import re

from utils import read_input


class Monkey:
    items: []
    operation = lambda x: x
    divisible_by: int
    sent_to_true: int
    sent_to_false: int


re_monkey = re.compile(
    '''\s*Monkey.*\n  Starting items:\s+(.+)\s+Operation: new = (.+)\n\s*Test: divisible by ([0-9]+)\n\s+If true: throw to monkey ([0-9]+)\n\s+If false: throw to monkey ([0-9]+)''')

re_operation_plus = re.compile('''old \+ ([0-9]+)''')
re_operation_mpty = re.compile('''old \* ([0-9]+)''')


def parse_operation(text: str):
    if text == 'old * old':
        return lambda x: x * x

    m = re_operation_plus.match(text)
    if m is not None:
        n = int(m[1])
        return lambda x: x + n

    m = re_operation_mpty.match(text)
    if m is not None:
        n = int(m[1])
        return lambda x: x * n

    m = re_operation_mpty.match(text)

    return None


def parse_monkey(text: str) -> Monkey:
    m = re_monkey.match(text)
    monkey = Monkey()
    monkey.items = [int(i) for i in m[1].split(', ')]
    monkey.operation = parse_operation(m[2])
    monkey.divisible_by = int(m[3])
    monkey.sent_to_true = int(m[4])
    monkey.sent_to_false = int(m[5])
    return monkey


def parse_monkeys(text: str):
    return [parse_monkey(b) for b in text.split('\n\n')]


def play_monkey(i, monkeys, worry_division):
    monkey = monkeys[i]
    for item in monkey.items:
        new_level = monkey.operation(item)
        new_level = new_level // worry_division
        if new_level % monkey.divisible_by == 0:
            monkeys[monkey.sent_to_true].items.append(new_level)
        else:
            monkeys[monkey.sent_to_false].items.append(new_level)
    monkey.items = []


def play_round(monkeys, monkey_activity, worry_division):
    for i, m in enumerate(monkeys):
        monkey_activity[i] += len(m.items)
        play_monkey(i, monkeys, worry_division)

    all_dividers = 1
    for d in [m.divisible_by for m in monkeys]:
        all_dividers *= d
    for m in monkeys:
        m.items = [i % all_dividers for i in m.items]


def print_monkeys(monkeys):
    for j in range(0, len(monkeys)):
        print('Monkey %d: %s' % (j, monkeys[j].items))
    print('\n')


if __name__ == '__main__':
    lines = read_input('input-a.txt')

    # part 1
    monkeys = parse_monkeys('\n'.join(lines))
    monkey_activity = [0 for i in range(0, len(monkeys))]
    for i in range(0, 20):
        play_round(monkeys, monkey_activity, 3)

    monkey_activity.sort()
    print(monkey_activity[-1] * monkey_activity[-2])

    # part 2
    monkeys = parse_monkeys('\n'.join(lines))
    monkey_activity = [0 for i in range(0, len(monkeys))]
    for i in range(0, 10000):
        play_round(monkeys, monkey_activity, 1)

    monkey_activity.sort()
    print(monkey_activity[-1] * monkey_activity[-2])
