from collections import deque
from datetime import datetime, timedelta
lst, time = input().split(";"), datetime.strptime(input(), "%H:%M:%S")
rbs, fre_rbs, pds = [], deque(), deque()
for i in lst:
    inf = i.split("-")
    rbt = {"name": inf[0], "speed": int(inf[1]), "available": time}
    rbs.append(rbt), fre_rbs.append(rbt)
while True:
    pdt = input()
    if pdt == "End":
        break
    pds.append(pdt)
time += timedelta(seconds=1)
while pds:
    cnt_pdt = pds.popleft()
    if fre_rbs:
        cnt_rbt = fre_rbs.popleft()
        cnt_rbt["available"] = time + timedelta(seconds=cnt_rbt["speed"])
        print(f"{cnt_rbt['name']} - {cnt_pdt} [{time.strftime('%H:%M:%S')}]")
    else:
        for r in rbs:
            if time >= r["available"]:
                fre_rbs.append(r)
        if not fre_rbs:
            pds.append(cnt_pdt)
        else:
            cnt_rbt = fre_rbs.popleft()
            cnt_rbt["available"] = time + timedelta(seconds=cnt_rbt["speed"])
            print(f"{cnt_rbt['name']} - {cnt_pdt} [{time.strftime('%H:%M:%S')}]")
    time += timedelta(seconds=1)
