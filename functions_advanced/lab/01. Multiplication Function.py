from functools import reduce
multiply = lambda *args: reduce(lambda x, y: x * y, args)
