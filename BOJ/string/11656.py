import sys
input = sys.stdin.readline
s = input().strip()
temp = []
for i in range(0, len(s)):
    temp.append(s[i:])
temp = sorted(temp)
for e in temp:
    print(e)
