from collections import deque
ppl = deque()
while True:
    cmd = input()
    if cmd == "End":
        print(f"{len(ppl)} people remaining.")
        break
    if cmd == "Paid":
        while ppl:
            print(ppl.popleft())
    else:
        ppl.append(cmd)
