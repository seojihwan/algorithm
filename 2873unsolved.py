# n,k = map(int,input().split())
def findmin(arr):
    idx_r = -1
    idx_c = -1
    i = 0
    min = 1000
    for k in range (len(arr)):
        if i % 2 == 1:
            i = 0
        else:
            i = 1
        while i < len(arr[0]):
            if min > arr[k][i]:
                min = arr[k][i]
                idx_r = i
                idx_c = k
            i += 2
    return idx_r, idx_c

n = list(map(int,input().split()))
R = n[0]
C = n[1]

arr = []
for i in range(n[1]):
    arr.append(list(map(int,input().split())))

a = ""
if R // 2 == 1 and C // 2 == 1:     # R C 홀 홀
    for k in range(R // 2):
        for i in range(C - 1):
            a += "D"
        a += "R"
        for i in range(C - 1):
            a += "U"
        a += "R"
    for i in range(C - 1):
        a += "D"

elif R // 2 == 1:
    for k in range (C - 2) / 2:
        for i in range(R - 1):
            a += "R"
        a += "D"
        for i in range(R - 1):
            a += "L"
        a += "D"
    for i in range(C // 2):
        a += "DRUR"
    a += "D"

elif C // 2 == 1:
    for k in range (R - 2) / 2:
        for i in range(C - 1):
            a += "D"
        a += "R"
        for i in range(C - 1):
            a += "U"
        a += "R"
    for i in range(C // 2):
        a += "RDLD"
    a += "R"
else:           # R C 짝 짝
    idx = findmin(arr)
    idx_r = 0
    idx_c = 0
    while idx_r <= idx[0] - 1:
        idx_r += 1
        a += "R"
    a += "D"
    idx_c += 1
    while idx_r <= R - 1:
        if idx_r == idx[0] + 1:
            a +="UR"
            idx_r += 1
            idx_c -= 1
        idx_r += 1
        a += "R"

    while idx_c < C:




    # if R == 2 and C == 2:
    #     if arr[0][1] > arr[1][0]:
    #         a = "RD"
    #     else :
    #         a = "DR"
    # elif R == 2:
    #     if arr[C - 1][0] == min(arr[C - 1][0], arr[0][1], arr[C - 2][1]):
    #         for i in range((C - 2) // 2):
    #             a +="RDLD"
    #         a += "RD"
    #     elif arr[0][1] == min(arr[C - 1][0], arr[0][1], arr[C - 2][1]):
    #         for i in range((C - 2) // 2):
    #             a += "DRDL"
    #         a += "DR"
    #     else :
    #         for i in range((C - 2) // 2):
    #             a += "RDLD"
    #         a += "DR"
    # elif C == 2:
    #     if arr[0][R - 1] == min(arr[0][R - 1], arr[1][0], arr[1][R - 2]):
    #         for i in range(R - 2) / 2:
    #             a +="DRUR"
    #         a += "DR"
    #     elif arr[1][0] == min(arr[0][R - 1], arr[1][0], arr[1][R - 2]):
    #         for i in range(R - 2) / 2:
    #             a += "RDRU"
    #         a += "RD"
    #     else :
    #         for i in range(R - 2) / 2:
    #             a +="DRUR"
    #         a += "RD"
    # else :
        



        
    # if n[0] == 2 and n[1] == 2:
    #     a = "DR"     # case 4가지 나누어서...
    # if n[0] < n[1]:
    #     for k in range (n[1] - 2) / 2:
    #         for i in range (n[0] - 1):
    #             a += "R"
    #         a += "D"
    #         for i in range (n[0] - 1):
    #             a += "L"
    #         a += "D"
    #     if arr[n[0] - 2][n[0] - 1] > arr[n[0] - 1][n[0] - 2]:
    #         a += "DR"
    #         for m in range (n[1] - 2) / 2:
    #             a += "URDR"
    #     else :
    #         a += "RD"
    #         for m in range (n[1] - 2) / 2:
    #             a += "URDR"
    # if arr[n[0] - 2][n[0] - 1] > arr[n[0] - 1][n[0] - 2]:


print(a)


# sign = input().split()
# arr = list(map(int,input().split()))
# exchange = [500, 100, 50, 10, 5, 1]
# def sol():
#     cnt = 0
#     global price
#     while price > 0:
#         for i in range(6):
#             while price >= exchange[i]:
#                 if price >= exchange[i]:
#                     price -= exchange[i]
#                     cnt += 1
#     return cnt

# print(sol())
