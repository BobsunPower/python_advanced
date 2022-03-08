# TODO
from collections import deque
row, col = [int(x) for x in input().split()]
deq = deque(list(input()))
mtx = []
for i in range(row):
    mtx.append([])
    for j in range(col):
        mtx[i].append("")
for i in range(row):
    for j in range(col):
        cnt_col = j
        cnt_chr = deq.popleft()
        if i % 2 != 0:
            cnt_col = col - 1 - j
        mtx[i][cnt_col] = cnt_chr
        deq.append(cnt_chr)
[print("".join(str(x) for x in row)) for row in mtx]
