def check(par):
    bks = ['()', '{}', '[]']
    while any(x in par for x in bks):
        for b in bks:
            par = par.replace(b, '')
    return not par


print("YES" if check(input()) else "NO")
