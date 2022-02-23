from collections import defaultdict
lst, dic = [], defaultdict(list)
for n in range(int(input())):
    std, grd = input().split()
    dic[std].append(float(grd))
[print(f"{k} -> {' '.join([f'{n:.2f}' for n in v])} (avg: {sum(v) / len(v):.2f})") for k, v in dic.items()]
