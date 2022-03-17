def math_operations(*arg, i=None, **kwa):
    if i is None:
        arg, i = tuple(map(int, arg)), 0
    if not arg:
        return kwa
    if i == 0:
        res = kwa['a'] + arg[0]
        kwa['a'] = res
    elif i == 1:
        res = kwa['s'] - arg[0]
        kwa['s'] = res
    elif i == 2:
        if arg[0] != 0:
            res = kwa['d'] / arg[0]
            kwa['d'] = res
    elif i == 3:
        res = kwa['m'] * arg[0]
        kwa['m'] = res
    return math_operations(*arg[1:], i=0 if i == 3 else i + 1, **kwa)
