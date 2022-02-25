lst, ptd = list(map(float, input().split())), []
[ptd.append(i) for i in lst if i not in ptd]
[print(f"{i} - {lst.count(i)} times") for i in ptd]
