from collections import deque
deq, n = deque(input().split()), int(input())
while len(deq) > 1:
    deq.rotate(-n), print(f"Removed {deq.pop()}")
print(f"Last is {deq.pop()}")
