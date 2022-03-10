from collections import deque


def find_player(fld):
    for r in range(len(fld)):
        for c in range(len(fld[r])):
            if fld[r][c] == "P":
                return r, c


def fnd_bns(fld):
    return [(r, c) for r in range(len(fld)) for c in range(len(fld[r])) if fld[r][c] == "B"]


def spr_bns(bns, fld):
    for r, c in bns:
        if r-1 in range(len(fld)):
            fld[r - 1][c] = "B"
        if r+1 in range(len(fld)):
            fld[r + 1][c] = "B"
        if c-1 in range(len(fld[0])):
            fld[r][c - 1] = "B"
        if c+1 in range(len(fld[0])):
            fld[r][c + 1] = "B"
    return fld


def play(fld, dns):
    psb_mvs = {
        "U": lambda row, col: (row - 1, col),
        "D": lambda row, col: (row + 1, col),
        "L": lambda row, col: (row, col - 1),
        "R": lambda row, col: (row, col + 1),
    }
    while dns:
        dtn = dns.popleft()
        r, c = find_player(fld)
        fld[r][c] = "."
        nxt_rol, nxt_col = psb_mvs[dtn](r, c)
        if nxt_rol not in range(len(fld)) or nxt_col not in range(len(fld[r])):
            fld = spr_bns(fnd_bns(fld), fld)
            res = '\n'.join([''.join(fld[r]) for r in range(len(fld))])
            res += f"\nwon: {r} {c}"
            return res
        fld = spr_bns(fnd_bns(fld), fld)
        if fld[nxt_rol][nxt_col] == "B":
            res = '\n'.join([''.join(fld[r]) for r in range(len(fld))])
            res += f"\ndead: {nxt_rol} {nxt_col}"
            return res
        fld[nxt_rol][nxt_col] = "P"


rows, cols = [int(n) for n in input().split()]
mtx, cmd = [list(input()) for _ in range(rows)], deque(input())
print(play(mtx, cmd))
