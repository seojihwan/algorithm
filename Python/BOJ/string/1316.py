from sys import stdin
input = stdin.readline
n = int(input())
cnt = n
for _ in range(n):
    temp = []
    s = input().strip()
    for i in range(1, len(s)):
        temp.append(s[0])
        if s[i - 1] != s[i]:
            if s[i] not in temp:
                temp.append(s[i - 1])
            else:
                cnt -= 1
                break
print(cnt)
