o, s = input(), []
for i, j in enumerate(o):
    s.append(i) if j == "(" else None
    print(o[s.pop():i + 1]) if j == ")" else None
