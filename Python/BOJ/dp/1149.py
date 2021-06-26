from sys import stdin
input = stdin.readline
n = int(input())
dp = [0] * 3
for _ in range(n):
    r, g, b = map(int, input().split())
    dp[0], dp[1], dp[2] = min(dp[1], dp[2]) + \
        r, min(dp[0], dp[2]) + g, min(dp[0], dp[1]) + b
print(min(dp))
