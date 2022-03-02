n = int(input())
m = [[int(n) for n in input().split(', ')] for _ in range(n)]
print(f'''Primary diagonal: {', '.join([str(m[i][i]) for i in range(n)])}. Sum: {sum([m[i][i] for i in range(n)])}
Secondary diagonal: {', '.join([str(m[i][n - 1 - i]) for i in range(n)])}. Sum: {sum([m[i][n-1-i] for i in range(n)])}''')
