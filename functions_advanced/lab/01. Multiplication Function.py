from functools import reduce
multiply = lambda *arg: reduce(lambda x, y: x * y, arg)
