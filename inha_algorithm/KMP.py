
# next 배열을 -1의 원소를 갖는 300의 크기로 초기화하였습니다.
next = [-1 for _ in range(300)]

# KMP 의 initNext함수입니다.


def initNext(a):
    j = -1
    for i in range(len(a)):
        # next[i] = j
        next[i] = (a[i] == a[j]) and next[j] or j
        while j >= 0 and a[i] != a[j]:
            j = next[j]
        j += 1

# KMP 함수입니다.


def KMP(p, t):
    initNext(p)
    i = 0
    j = 0
    while j < len(p) and i < len(t):
        while j >= 0 and t[i] != p[j]:
            j = next[j]
        i += 1
        j += 1
    if j == len(p):
        return i - len(p)
    else:
        return i


# 입력 받는 과정입니다.
pattern = list(input())
texts = []
while 1:
    text = list(input())
    if text == ['0']:
        break
    texts.append(text)

# KMP함수를 실행해서 구해낸 pos값을 저장합니다.
temp = []
for k in range(len(texts)):
    i = 0
    prev = 0
    while 1:
        pos = KMP(pattern, texts[k][i:])
        pos += prev
        i = pos + len(pattern)
        if i <= len(texts[k]):
            temp.append([pos, k])
        else:
            break
        prev = i

# 정렬 후 출력 조건에 맞게 출력합니다.
temp.sort(key=lambda x: x[0])
for k in range(len(temp)):
    print(''.join(texts[temp[k][1]]))

