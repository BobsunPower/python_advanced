par, bks = input(), ['()', '{}', '[]']
while any(x in par for x in bks):
    for b in bks:
        par = par.replace(b, '')
print("NO" if par else "YES")
