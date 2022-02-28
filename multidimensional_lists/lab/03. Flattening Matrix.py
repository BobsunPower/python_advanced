from itertools import chain
print([n for n in chain(*[[int(n) for n in input().split(', ')] for _ in range(int(input()))])])
