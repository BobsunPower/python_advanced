sqr = int(input())
mtx = [[int(n) for n in input().split()] for _ in range(sqr)]
print(sum([mtx[i][i] for i in range(sqr)]))
