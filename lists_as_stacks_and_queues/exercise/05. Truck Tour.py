from collections import deque
deq = deque(x - y for x, y in [list(map(int, input().split())) for n in range(int(input()))])
for i in range(len(deq)):
    gas = 0
    for pmp in deq:
        gas += pmp
        if gas < 0:
            break
    if gas >= 0:
        print(i)
        break
    else:
        deq.append(deq.popleft())
