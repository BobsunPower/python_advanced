def even_odd(*arg):
    cmd, lst = arg[-1], [n for n in arg if str(n).isdigit()]
    return [n for n in lst if n % 2 == 1] if cmd == 'odd' else [n for n in lst if n % 2 == 0]
