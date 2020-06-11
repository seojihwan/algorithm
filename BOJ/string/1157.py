import sys
input = sys.stdin.readline
w = input().strip().lower()
arr = [[0, chr(97 + i)] for i in range(26)]
for e in w:
    arr[ord(e) - 97][0] += 1
arr = sorted(arr, reverse=True)
if arr[0][0] != arr[1][0]:
    print(arr[0][1].upper())
else:
    print("?")
