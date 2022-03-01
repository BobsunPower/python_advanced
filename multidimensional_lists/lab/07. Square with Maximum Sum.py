from itertools import chain
row, col = map(int, input().split(', '))
mtx, sqs, mxm, bst, nbr = [[int(n) for n in input().split(', ')] for _ in range(row)], [], 0, 0, 0
for i in range(len(mtx) - 1):
    for j in range(len(mtx[i]) - 1):
        sqr = [mtx[i][j], mtx[i][j + 1]], [mtx[i + 1][j], mtx[i + 1][j + 1]]
        sqs.append(sqr)
for s in sqs:
    nbr = sum(chain(*s))
    if nbr > mxm:
        mxm, bst = nbr, s
print("\n".join([' '.join(map(str, x)) for x in bst]), '\n', sum(list(map(sum, list(bst)))))
