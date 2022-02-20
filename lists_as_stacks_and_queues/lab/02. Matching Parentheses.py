stk, fi = input(), []
for i, j in enumerate(stk):
    fi.append(i) if j == "(" else None
    print(stk[fi.pop():i + 1]) if j == ")" else None
