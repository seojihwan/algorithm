def rotate(sentence, rot):
    if rot > 0:
        for _ in range(rot):
            temp = sentence[0]
            for i in range(1, len(sentence)):
                sentence[i-1] = sentence[i]
            sentence[-1] = temp
    elif rot < 0:
        for _ in range(abs(rot)):
            temp = sentence[-1]
            for i in range(len(sentence)-2, -1, -1):
                sentence[i+1] = sentence[i]
            sentence[0] = temp


def keytonum(key):
    nums = []
    temp = list(key)
    while temp:
        s = temp.pop(0)
        nums.append(ord(s)-96)
    return nums


def solution(encrypted_text, key, rotation):
    nums = keytonum(key)
    enc = list(encrypted_text)
    res = []

    rotate(enc, rotation)
    while enc:
        s = enc.pop(0)
        num = nums.pop(0)
        if (ord(s)-num) < 97:
            res.append(chr(ord(s)-num+26))
        else:
            res.append(chr(ord(s)-num))

    answer = ''
    for e in res:
        answer += e
    return answer
