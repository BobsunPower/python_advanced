f, s = list(map(int, input().split()))
fst, sec = set(), set()
[fst.add(input()) for _ in range(f)]
[sec.add(input()) for _ in range(s)]
print('\n'.join(fst & sec))
