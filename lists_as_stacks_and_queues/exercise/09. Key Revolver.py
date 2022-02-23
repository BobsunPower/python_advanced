from collections import deque
prc, brl, sts = int(input()), int(input()), 0
bts, lks, itg = list(map(int, input().split())), deque(map(int, input().split())), int(input())
while lks and bts:
    blt, lok = bts.pop(), lks.popleft()
    sts += 1
    if blt > lok:
        print("Ping!")
        lks.appendleft(lok)
    else:
        print("Bang!")
    if sts % brl == 0 and bts:
        print("Reloading!")
if not lks:
    print(f"{len(bts)} bullets left. Earned ${itg - (sts * prc)}")
elif not bts:
    print(f"Couldn't get through. Locks left: {len(lks)}")
