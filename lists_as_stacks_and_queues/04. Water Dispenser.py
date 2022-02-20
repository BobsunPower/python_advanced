from collections import deque
deq, dic, qty = deque(), {}, int(input())
while True:
    cmd = input()
    if cmd == "Start":
        while True:
            cmd = input()
            if cmd == "End":
                for k, v in dic.items():
                    if v <= qty:
                        qty -= v
                        print(f"{k} got water")
                    else:
                        print(f"{k} must wait")
                print(f"{qty} liters left")
                exit()
            if "refill" in cmd:
                qty += int(cmd.split()[1])
            if cmd.isdigit():
                dic[deq.popleft()] = int(cmd)
    deq.append(cmd)
