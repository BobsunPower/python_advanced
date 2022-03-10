from collections import deque


def fnd_mnr(fld):
    for r in range(len(fld)):
        for c in range(len(fld[r])):
            if fld[r][c] == "s":
                return r, c


def lft_col(fld):
    x = 0
    for r in range(len(fld)):
        for c in range(len(fld[r])):
            if fld[r][c] == "c":
                x += 1
    return x


def move(fld, dns):
    psb_mvs = {
        "up": lambda row, col: (row - 1, col),
        "down": lambda row, col: (row + 1, col),
        "left": lambda row, col: (row, col - 1),
        "right": lambda row, col: (row, col + 1),
    }
    while dns:
        dtn = dns.popleft()
        r, c = fnd_mnr(fld)
        fld[r][c] = "*"
        nxt_row, nxt_col = psb_mvs[dtn](r, c)
        if nxt_row not in range(len(fld)) or nxt_col not in range(len(fld[r])):
            fld[r][c] = "s"
            continue
        if fld[nxt_row][nxt_col] == "e":
            return f"Game over! ({nxt_row}, {nxt_col})"
        fld[nxt_row][nxt_col] = "s"
        if not lft_col(fld):
            return f"You collected all coal! ({nxt_row}, {nxt_col})"
    r, c = fnd_mnr(fld)
    rmn_col = lft_col(fld)
    return f"{rmn_col} pieces of coal left. ({r}, {c})"


rows = int(input())
dirs = deque(input().split())
mtx = [input().split() for _ in range(rows)]
print(move(mtx, dirs))
