import sys
from collections import defaultdict, deque
input = sys.stdin.readline

num = 1
flag2 = True
while flag2:
    parent = defaultdict(int)
    child = defaultdict(list)
    flag = True
    nodeset = set()
    while flag:
        lines = list(map(int, input().split()))
        for i in range(len(lines) // 2):
            if lines[i * 2] == -1 and lines[i * 2 + 1] == -1:
                flag, flag2 = False, False
                break
            if not lines[i * 2] and not lines[i * 2 + 1]:
                flag = False
                break
            parent[lines[i * 2 + 1]] += 1
            parent[lines[i * 2]]
            child[lines[i * 2]].append(lines[i * 2 + 1])
            nodeset.add(lines[i * 2])
            nodeset.add(lines[i * 2 + 1])
    print(parent)
    if not flag2:
        break
    rootcnt = 0
    res = True
    root = 0
    for k in parent.keys():
        if not parent[k]:
            root = k
            rootcnt += 1
        elif parent[k] >= 2:
            res = False
            break
    if root:
        visited = set()
        visited.add(root)
        q = deque([root])
        while q:
            s = q.popleft()
            for node in child[s]:
                if node not in visited:
                    q.append(node)
                    visited.add(node)
    if (rootcnt != 1 and len(parent)):
        res = False
    if root and len(visited) != len(nodeset):
        res = False
    if res:
        print('Case', num, 'is a tree')
    else:
        print('Case', num, 'is not a tree')

    num += 1
