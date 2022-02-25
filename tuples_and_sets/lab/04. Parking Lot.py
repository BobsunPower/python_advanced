s = set()
for _ in range(int(input())):
    cmd, reg = input().split(", ")
    s.add(reg) if cmd == "IN" else s.remove(reg)
print('\n'.join(s)) if s else print("Parking Lot is Empty")
