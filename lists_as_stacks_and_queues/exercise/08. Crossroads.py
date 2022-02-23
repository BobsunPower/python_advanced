from collections import deque
sec, xtr, crs, psd, csh = int(input()), int(input()), deque(), 0, False
while True:
    cmd, s, x = input(), sec, xtr
    if csh or cmd == "END":
        break
    crs.append(cmd) if cmd != "green" else None
    while cmd == "green" and s > 0:
        if crs:
            car = crs.popleft()
            c, car = car, list(car)
        else:
            break
        for i in range(len(car)):
            ch = car.pop(0)
            if len(car) == 0:
                psd += 1
            s -= 1
            if s < 0:
                x -= 1
                if x < 0:
                    print(f"A crash happened!\n{c} was hit at {ch}.")
                    csh = True
                    break
print(f"Everyone is safe.\n{psd} total cars passed the crossroads." if not csh else '')
