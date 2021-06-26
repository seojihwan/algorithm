def solution(encrypted_text, key, rotation):
    answer = ''
    temp = ''
    for idx, e in enumerate(encrypted_text):
        i = (idx + rotation) % len(encrypted_text)
        temp += encrypted_text[i]
    for i in range(len(key)):
        cnt = (ord(temp[i]) - (ord(key[i]) - 96) + 26)
        if cnt >= 123:
            cnt -= 26
        answer += chr(cnt)
    return answer
