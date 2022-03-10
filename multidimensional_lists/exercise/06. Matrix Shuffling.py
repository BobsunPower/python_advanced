row, _ = [int(i) for i in input().split()]
mtx = [[i for i in input().split()] for i in range(row)]
while True:
    cmd = input()
    if cmd == "END":
        break
    if "swap" not in cmd or len(cmd.split()) != 5:
        print("Invalid input!")
    else:
        n = [int(i) for i in cmd.split()[1:]]
        lst = [item for item in n if item < 0 or item > len(mtx)]
        if len(lst) > 0:
            print("Invalid input!")
        else:
            mtx[n[0]][n[1]], mtx[n[2]][n[3]] = mtx[n[2]][n[3]], mtx[n[0]][n[1]]
            [print(*i) for i in mtx]
