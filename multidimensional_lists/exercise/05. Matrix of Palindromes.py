row, col = map(int, input().split())
alp = list(map(chr, range(97, 123)))
[print(*[f'{alp[i]}{alp[j]}{alp[i]}' for j in range(i, col + i)], sep=' ') for i in range(row)]
