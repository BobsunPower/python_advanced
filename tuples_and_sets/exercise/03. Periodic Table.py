s = set()
[s.add(e) for _ in range(int(input())) for e in input().split(" ")]
print("\n".join(s))
