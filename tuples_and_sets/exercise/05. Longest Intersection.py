fst_set, sec_set, bst, cnt = set(), set(), "", ""
for _ in range(int(input())):
    fst, mid, fth = input().split(",")
    sec, trd = str(mid).split("-")
    fst, sec, trd, fth = int(fst), int(sec), int(trd), int(fth)
    [fst_set.add(x) for x in range(fst, sec + 1)]
    [sec_set.add(y) for y in range(trd, fth + 1)]
    cnt = fst_set & sec_set
    bst = cnt if len(cnt) > len(bst) else bst
    fst_set.clear(), sec_set.clear()
print(f"Longest intersection is {list(bst)} with length {len(bst)}")
