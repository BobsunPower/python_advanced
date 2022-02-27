lst, tot, evn, odd = [], 0, set(), set()
for i in range(1, int(input()) + 1):
    lst = [(sum(ord(letter) for letter in input()))]
    res = sum(lst) // i
    lst.clear()
    evn.add(res) if res % 2 == 0 else odd.add(res)
print(", ".join(str(x) for x in (evn | odd))) if sum(evn) > sum(odd) else None
print(", ".join(str(x) for x in (odd - evn))) if sum(evn) < sum(odd) else None
print(", ".join(str(x) for x in (odd | evn))) if sum(evn) == sum(odd) else None
