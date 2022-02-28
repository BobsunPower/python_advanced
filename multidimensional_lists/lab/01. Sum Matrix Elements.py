row, _ = map(int, input().split(', '))
mtx = [[int(n) for n in input().split(', ')] for _ in range(row)]
print(sum([sum(lst) for lst in mtx]), '\n', mtx)
