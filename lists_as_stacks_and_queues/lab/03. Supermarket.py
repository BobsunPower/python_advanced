from collections import deque
deq = deque()
while True:
    cmd = input()
    if cmd == "End":
        print(f"{len(deq)} people remaining.")
        break
    if cmd == "Paid":
        while deq:
            print(deq.popleft())
    else:
        deq.append(cmd)
