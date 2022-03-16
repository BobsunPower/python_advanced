def fill_the_box(hgt, lth, wth, *arg, spc=None):
    arg = list(arg)
    spc = int(hgt) * int(wth) * int(lth) if spc is None else spc
    if arg[0] == "Finish":
        return f"There is free space in the box. You could put {spc} more cubes."
    elif spc - int(arg[0]) <= 0:
        arg[0] -= spc
        return f"No more free space! You have {sum(map(int, arg[:arg.index('Finish')]))} more cubes."
    return fill_the_box(hgt, lth, wth, *arg[1:], spc=spc - int(arg[0]))
