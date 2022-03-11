def sorting_cheeses(**kwa):
    dic, out = {k: v for k, v in sorted(kwa.items(), key=lambda i: len(i[1])).__reversed__()}, ''
    for k, v in dic.items():
        out += f'\n{k}\n' + '\n'.join([str(i) for i in sorted(v).__reversed__()])
    return out
