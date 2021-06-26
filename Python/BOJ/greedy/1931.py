import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    s, e = input().split()
    arr.append((int(s), int(e)))
arr.sort()
cnt = 1
end = arr[0][1]

for i in range(1, n):
    if end > arr[i][1]:
        end = arr[i][1]
    elif end <= arr[i][0]:
        end = arr[i][1]
        cnt += 1
print(cnt)
