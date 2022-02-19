x, s = input(), []
for i, j in enumerate(x):
    s.append(i) if j == "(" else None
    print(x[s.pop():i + 1]) if j == ")" else None
