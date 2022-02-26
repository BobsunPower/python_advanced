from collections import defaultdict
dic = defaultdict(int)
for c in input():
    dic[c] += 1
[print(f"{c}: {n} time/s") for c, n in sorted(dic.items())]
