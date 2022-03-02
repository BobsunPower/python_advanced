n = int(input())
m = [[int(n) for n in input().split()] for _ in range(n)]
print(abs(sum([m[i][n-1-i] for i in range(n)]) - sum([m[i][i] for i in range(n)])))
