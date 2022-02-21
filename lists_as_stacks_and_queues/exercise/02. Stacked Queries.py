from collections import deque
stk = deque()
for i in range(int(input())):
    cmd = list(map(int, input().split()))
    stk.appendleft(int(cmd[1])) if cmd[0] == 1 else None
    stk.popleft() if cmd[0] == 2 and stk else None
    print(max(stk)) if cmd[0] == 3 and stk else None
    print(min(stk)) if cmd[0] == 4 and stk else None
print(f"{', '.join(map(str, stk))}")
