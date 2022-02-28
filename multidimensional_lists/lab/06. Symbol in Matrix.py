mtx, sch, row, col = [list(input()) for _ in range(int(input()))], input(), 0, 0
for r, i in enumerate(mtx):
    if row:
        break
    for c, j in enumerate(i):
        if j == sch:
            row, col = r, c
print(f"({row}, {col})" if row else f"{sch} does not occur in the matrix")
