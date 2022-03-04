row, col = map(int, input().split())
m, out, mxm = [[int(n) for n in input().split()] for _ in range(row)],  '', -9223372036854775807
for i in range(row - 2):
    for j in range(col - 2):
        fst = [m[i][j], m[i][j + 1], m[i][j + 2]]
        sec = [m[i + 1][j], m[i + 1][j + 1], m[i + 1][j + 2]]
        trd = [m[i + 2][j], m[i + 2][j + 1], m[i + 2][j + 2]]
        if sum(fst) + sum(sec) + sum(trd) > mxm:
            mxm = sum(fst) + sum(sec) + sum(trd)
            out = f'''{' '.join(map(str, fst))}\n{' '.join(map(str, sec))}\n{' '.join(map(str, trd))}'''
print(f"Sum = {mxm}", '\n' + out)
