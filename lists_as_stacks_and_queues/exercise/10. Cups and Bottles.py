from collections import deque
cps, bts, wtd = deque((map(int, input().split()))), list(map(int, input().split())), 0
while bts:
    btl, cup = bts.pop(), cps.popleft()
    if btl >= cup:
        wtd += (btl - cup)
    else:
        cup -= btl
        cps.appendleft(cup)
    if not cps:
        print(f'Bottles: {" ".join(map(str, bts))}')
        break
    if not bts:
        print(f'Cups: {" ".join(map(str, cps))}')
        break
print(f"Wasted litters of water: {wtd}")
