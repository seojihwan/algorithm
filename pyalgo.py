
# n,k = map(int,input().split())
count = int(input())

sign = input().split()
sol = [0 for i in range(count + 1)]
sol2 = [0 for i in range(count + 1)]

def max_solve():
    max_num = 9
    cnt = 0
    for i in range(count - 1):
        if sign[i] == '<' and sign[i + 1] == '<':
            if i == 0 :
                sol[0] = 7
                sol[1] = 8
                sol[2] = 9
            else :
                for k in range(i):
                    if sign[i - k - 1] == '<':
                        cnt +=1
                    else:
                        break
                for m in range(cnt):
                    sol[i - m - 1] -= 1
                
                sol[i + 2] = sol[i + 1]
                sol[i + 1] -= 1
                sol[i] -= 1
            cnt = 0
        elif sign[i] == '<' and sign[i + 1] == '>':
            if i == 0 :
                sol[0] = 8
                sol[1] = 9
                sol[2] = 7
            else :
                sol[i + 2] = max_num - (i + 2)

        elif sign[i] == '>' and sign[i + 1] == '<':
            if i == 0 :
                sol[0] = 9
                sol[1] = 7
                sol[2] = 8
            else :
                sol[i + 2] = sol[i + 1]
                sol[i + 1] -= 1
        elif sign[i] == '>' and sign[i + 1] == '>':
            if i == 0 :
                sol[0] = 9
                sol[1] = 8
                sol[2] = 7
            else :
                sol[i + 2] = max_num - (i + 2)
def min_solve():
    min_num = 0
    cnt = 0
    for i in range(count - 1):
        if sign[i] == '<' and sign[i + 1] == '<':
            if i == 0 :
                sol2[0] = 0
                sol2[1] = 1
                sol2[2] = 2
            else :
                sol2[i + 2] = min_num + (i + 2)
        elif sign[i] == '<' and sign[i + 1] == '>':
            if i == 0 :
                sol2[0] = 0
                sol2[1] = 2
                sol2[2] = 1
            else :
                sol2[i + 2] = sol2[i + 1]
                sol2[i + 1] += 1
        elif sign[i] == '>' and sign[i + 1] == '<':
            if i == 0 :
                sol2[0] = 1
                sol2[1] = 0
                sol2[2] = 2
            else :
                sol2[i + 2] = min_num + (i + 2)
        elif sign[i] == '>' and sign[i + 1] == '>':
            if i == 0 :
                sol2[0] = 2
                sol2[1] = 1
                sol2[2] = 0
            else :
                for k in range(i):
                    if sign[i - k - 1] == '>':
                        cnt +=1
                    else:
                        break
                for m in range(cnt):

                    sol2[i - m - 1] += 1
                sol2[i + 2] = sol2[i + 1]
                sol2[i + 1] += 1
                sol2[i] += 1
                cnt = 0

max_solve()
min_solve()
str_max = list(map(str, sol))
str_min = list(map(str, sol2))

# print(str_sol)
# b = ""
# for k in str_sol:
#     b += str(k)
# print(b)
print(''.join(str_max))
print(''.join(str_min))


    # grade = [[int(x) for x in input().split()] for y in range(v_num)]
    # grade.sort(key = lambda x : x[0])




