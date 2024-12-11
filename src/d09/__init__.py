from utils import read_input


def map_disk(inp: str):
    mem = []
    p = 0
    for i in range(0, len(inp), 2):
        mem.append((int(i / 2), p, int(inp[i])))
        p += int(inp[i])
        if i < len(inp) - 1:
            p += int(inp[i + 1])
    return mem


def pop_mem(mem: list[tuple]):
    id, pos, n = mem[-1]
    if (n > 1):
        mem[-1] = (id, pos, n - 1)
    else:
        mem.pop()
    return (pos + n - 1), id


def checksum(mem: list[tuple]) -> int:
    p = 0
    tot = 0
    i_block = 0
    p_tail = mem[-1][1] + mem[-1][2]
    while p_tail >= p + 1 and i_block < len(mem):
        id_block, p_block, len_block = mem[i_block]
        for i in range(len_block):
            tot += p * id_block
            # print(f'> {p}\t{id_block}\t{tot}')
            p += 1
        if i_block >= len(mem) - 1:
            break
        len_gap = mem[i_block + 1][1] - p
        i_block += 1
        while len_gap > 0 and p_tail > p + 1:
            p_tail, id_tail = pop_mem(mem)
            tot += p * id_tail
            # print(f'< {p}\t{p_tail}\t{id_tail}\t{tot}')

            len_gap -= 1
            p += 1

    return tot


def checksum_2(mem):
    i_block_dec = len(mem) - 1

    while i_block_dec > 0:
        id_block, p_block, len_block = mem[i_block_dec]
        print(f'trsying to move {mem[i_block_dec]}')
        idx = [i for i, b in enumerate(mem) if b[1] < p_block and len_block <= (mem[i + 1][1] - b[1] - b[2])]
        i_insert = idx[0] if idx else None
        if i_insert is not None:
            print(f'Moving {mem[i_block_dec]} after {mem[i_insert]}')
            b = mem.pop(i_block_dec)
            mem.insert(i_insert + 1, (b[0], mem[i_insert][1] + mem[i_insert][2], b[2]))
        else:
            i_block_dec -= 1

    for b1, b2 in zip(mem, mem[1:]):
        if b1[1] + b1[2] > b2[1]:
            print(f'BORDEL {b1} {b2}')

    tot = 0
    for b in mem:
        for i in range(b[2]):
            tot += (b[1] + i) * b[0]
    return tot


if __name__ == '__main__':
    # input = '12345'
    # input = '2333133121414131402'
    input = read_input('input-a.txt')[0]

    mem = map_disk(input)
    print(checksum(mem))

    mem = map_disk(input)
    print(checksum_2(mem))
