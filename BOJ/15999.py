row, col = map(int, input().split())

t = [(input()) for _ in range(row)]
print(t)
print(t[1][1])
cnt = 0
for a in range(row):
    for b in range(col):
        cnt += (not a or t[a][b] == t[a-1][b]) and (not b or t[a][b] == t[a][b-1]) and (
            a == row-1 or t[a][b] == t[a+1][b]) and (b == col-1 or t[a][b] == t[a][b+1])

print(2**cnt % (10**9 + 7))
