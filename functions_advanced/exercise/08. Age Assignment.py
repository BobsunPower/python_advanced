def age_assignment(*arg, **kwa):
    return {arg: kwa.get(arg[0]) for arg in arg}
