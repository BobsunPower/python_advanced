cmd, lst, odd, evn = input(), list(map(int, input().split())), [], []
[odd.append(n) if n % 2 == 1 else evn.append(n) for n in lst]
print(f"{sum(odd) * len(lst) if cmd == 'Odd' else sum(evn) * len(lst)}")
