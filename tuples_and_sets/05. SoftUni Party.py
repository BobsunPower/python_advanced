inv = set()
[inv.add(input()) for _ in range(int(input()))]
while True:
    cmd = input()
    if cmd == "END":
        break
    inv.remove(cmd) if cmd in inv else None
print(len(inv), '\n', '\n'.join(sorted(inv)))
