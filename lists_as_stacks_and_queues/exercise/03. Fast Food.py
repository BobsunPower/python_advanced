from collections import deque
qty, ods = int(input()), deque(map(int, input().split()))
print(max(ods))
while ods:
    if ods[0] > qty:
        break
    qty -= ods.popleft()
print(f'Orders left: {" ".join(map(str, ods))}' if ods else 'Orders complete')
