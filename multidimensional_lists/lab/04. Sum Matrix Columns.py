row, col = map(int, input().split(', '))
mtx, out = [[int(n) for n in input().split()] for _ in range(row)], 0
for c in range(col):
    for r in range(row):
        out += mtx[r][c]
    print(out)
    out = 0
