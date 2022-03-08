def valid_command() -> bool:
    if pos[0] != 'swap':
        return False
    if len(pos) != 5:
        return False
    ids = [int(x) for x in pos[1:]]
    if min(ids) < 0:
        return False
    z, x, c, v = ids
    if max(z, c) > row - 1:
        return False
    if max(x, v) > col - 1:
        return False
    return True


def print_matrix(data: list) -> None:
    for i in data:
        print(*i, sep=' ')


row, col = [int(x) for x in input().split()]
mtx = [[x for x in input().split()] for _ in range(row)]
while True:
    cmd = input()
    if cmd == 'END':
        break
    pos = cmd.split()
    if valid_command():
        q, w, e, r = [int(x) for x in pos[1:]]
        mtx[q][w], mtx[e][r] = mtx[e][r], mtx[q][w]
        print_matrix(mtx)
    else:
        print('Invalid input!')
