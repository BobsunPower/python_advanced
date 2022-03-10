from collections import deque
row, col = [int(x) for x in input().split()]
deq, mtx = deque(input()), []
for i in range(row):
    mtx.append([])
    for j in range(col):
        mtx[i].append("")
for i in range(row):
    for j in range(col):
        cnt_col, cnt_chr = j, deq.popleft()
        cnt_col = col - 1 - j if i % 2 != 0 else cnt_col
        mtx[i][cnt_col] = cnt_chr
        deq.append(cnt_chr)
[print("".join(str(i) for i in row)) for row in mtx]
