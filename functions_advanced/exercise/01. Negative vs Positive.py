lst, pos, neg = list(map(int, input().split())), [], []
[pos.append(n) if n > 0 else neg.append(n) for n in lst]
mor, les = ['negatives', 'positives'] if abs(sum(neg)) > sum(pos) else ['positives', 'negatives']
print(f"{sum(neg)}\n{sum(pos)}\nThe {mor} are stronger than the {les}")
