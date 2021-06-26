cn = int(input())
c = list(map(int, input().split()))
bn = int(input())
b = list(map(int, input().split()))

mem = [0] * 40001
able = []

for e in c:
    for i in range(len(able)):
        el = able[i]
        if not mem[abs(el - e)]:
            mem[abs(el - e)] = 1
            able.append(abs(el - e))
        if el + e < 15001 and not mem[el + e]:
            mem[el + e] = 1
            able.append(el + e)
    if not mem[e]:
        mem[e] = 1
        able.append(e)
for e in b:
    if mem[e]:
        print("Y", end=" ")
    else:
        print("N", end=" ")
