row, _ = map(int, input().split(', '))
mtx = [[int(n) for n in input().split(', ')] for _ in range(row)]
print(sum([sum(r) for r in mtx]), '\n', mtx)
