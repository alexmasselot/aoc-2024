import re

from utils import read_input, read_input_blocks


class Wiring:
    x: int
    y: int
    t: int
    wires: dict
    nb_z_bits: int

    def __init__(self):
        self.x = 0
        self.y = 0
        self.wires = {}

    def __str__(self):
        for i in range(self.nb_z_bits):
            k = 'z' + str(i).rjust(2, '0')
            print(f'{k}: {self.wires[k]}')
        o = f'''x: {format(self.x, 'b').rjust(self.nb_z_bits - 1, '0')}
y: {format(self.y, 'b').rjust(self.nb_z_bits - 1, '0')}
s: {format(self.x + self.y, 'b').rjust(self.nb_z_bits - 1, '0')}
z: {format(self.z(), 'b').rjust(self.nb_z_bits - 1, '0')}
'''

        return o

    def __getitem__(self, item: str):
        if item.startswith('x'):
            b = int(item[1:])
            return self.x & (1 << b) != 0
        if item.startswith('y'):
            b = int(item[1:])
            return self.y & (1 << b) != 0
        return self.wires[item]

    def compute(self, k: str):
        kv = self[k]
        if isinstance(kv, bool):
            return kv
        a, b, op = kv
        av = self.compute(a)
        bv = self.compute(b)
        if op == 'XOR':
            return av ^ bv
        if op == 'OR':
            return av | bv
        if op == 'AND':
            return av & bv
        print('FUCK')

    def z(self):
        r = 0
        for i in range(self.nb_z_bits):
            k = 'z' + str(i).rjust(2, '0')
            if self.wires[k]:
                r += 1 << i

        return r

    def check(self):
        if (self.x+ self.y) == self.z():
            print('OK')
        else:
            print('NOPE')

    def swap(self, a, b):
        t = self.wires[b]
        self.wires[b] = self.wires[a]
        self.wires[a] = t

    def to_svg(self, file: str):
        xs = ['x' + str(i).rjust(2, '0') + ' [color=pink,style=filled]' for i in range(self.nb_z_bits - 1)]
        ys = ['y' + str(i).rjust(2, '0') + ' [color=lightgreen,style=filled]' for i in range(self.nb_z_bits - 1)]
        zs = ['z' + str(i).rjust(2, '0') + ' [color=orange,style=filled]' for i in range(self.nb_z_bits)]
        with open(file, 'w') as fd:
            fd.write(f'''digraph g{{
{{
  {'\n  '.join(xs)}
}}
{{
  {'\n  '.join(ys)}
}}
{{
  {'\n  '.join(zs)}
}}
''')
            color = {
                'AND': 'red',
                'OR': 'green',
                'XOR': 'blue'
            }
            for t, ts in self.wires.items():
                print(f'{t} {ts}')
                (a, b, op) = ts
                fd.write(f'{{{a} {b}}} -> {t} [color={color[op]}]\n')

            fd.write('}\n')


def read_wiring(init_input: str, dep_input: str):
    wiring = Wiring()
    for l in init_input.split('\n'):
        t = l.split(': ')
        if t[0].startswith('x'):
            b = int(t[0][1:])
            if t[1] == '1':
                wiring.x = wiring.x | (1 << b)
        if t[0].startswith('y'):
            b = int(t[0][1:])
            if t[1] == '1':
                wiring.y = wiring.y | (1 << b)

    rx = r'''([a-z0-9]+) ([A-Z]+) ([a-z0-9]+) .> ([a-z0-9]+)'''

    for l in dep_input.split('\n'):
        m = re.match(rx, l)
        wiring.wires[m.group(4)] = (m.group(1), m.group(3), m.group(2))

    wiring.nb_z_bits = len([k for k in wiring.wires.keys() if k.startswith('z')])
    return wiring


if __name__ == '__main__':
    blocks = read_input_blocks('input.txt')
    wiring = read_wiring(blocks[0], blocks[1])

    wiring.swap('hmk', 'z16')
    wiring.swap('fcd', 'z33')
    wiring.swap('fhp', 'z20')
    wiring.swap('rvf', 'tpc')
    #fcd,fhp,hmk,rvf,tpc,z16,z20,z33
    wiring.to_svg('input.dot')

    zs = [k for k in wiring.wires.keys() if k.startswith('z')]
    zs.sort()
    zs.reverse()
    for z in zs:
        wiring.wires[z] = wiring.compute(z)
    print(wiring)
    print(wiring.z())
    wiring.check()

# lines = read_input('input-a.txt')

# OR green
# XOR blue
# AND RED
# hmk,z16
