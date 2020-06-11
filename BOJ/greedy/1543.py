import sys
input = sys.stdin.readline
t = input().strip()
p = input().strip()
start = 0
end = 0
cnt = 0
while end < len(t):
    if p in t[start: end + 1]:
        start = end + 1
        end += 1
        cnt += 1
    else:
        end += 1
print(cnt)
