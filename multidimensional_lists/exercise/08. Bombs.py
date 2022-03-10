mtx = [[int(n) for n in input().split()] for _ in range(int(input()))]
pos = [[int(n) for n in c.split(",")] for c in input().split()]
for bmb in pos:
    row, col = bmb
    if mtx[row][col] > 0:
        pwr = mtx[row][col]
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r in range(len(mtx)) and c in range(len(mtx[r])) and mtx[r][c] > 0:
                    mtx[r][c] -= pwr
cls = [mtx[r][c] for r in range(len(mtx)) for c in range(len(mtx[r])) if mtx[r][c] > 0]
print(f"Alive cells: {len(cls)}\nSum: {sum(cls)}")
[print(' '.join([str(n) for n in mtx[r]])) for r in range(len(mtx))]
