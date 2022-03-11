from functools import reduce
dic = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x / y, }
operate = lambda act, *arg: reduce(dic[act], arg)
