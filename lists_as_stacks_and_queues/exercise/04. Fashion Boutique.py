from collections import deque
stk, cap, cnt, rks = deque(map(int, input().split())), int(input()), 0, 1
while stk:
    clo = stk.popleft()
    if cnt + clo <= cap:
        cnt += clo
    else:
        rks += 1
        cnt = clo
print(rks)
