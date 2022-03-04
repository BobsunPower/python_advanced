row, col = map(int, input().split())
mtx, sqs = [[i for i in input().split()] for _ in range(row)], 0
for i in range(row-1):
    for j in range(col-1):
        sqs += 1 if mtx[i][j] == mtx[i+1][j] == mtx[i][j+1] == mtx[i+1][j+1] else 0
print(sqs)
