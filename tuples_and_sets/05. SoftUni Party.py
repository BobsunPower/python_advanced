inv = set()
for _ in range(int(input())):
    inv.add(input())
while True:
    cmd = input()
    if cmd == "END":
        break
    if cmd in inv:
        inv.remove(cmd)
print(len(inv))
print("\n".join(sorted(inv)))
