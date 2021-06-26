from collections import Counter


while True:
    temp = []
    isYes = True
    s = input()
    if len(s) == 1 and s == ".":
        break
    if Counter(s)["("] != Counter(s)[")"]:
        print("no")
        continue
    if Counter(s)["["] != Counter(s)["]"]:
        print("no")
        continue
    for e in s:
        if e == "(" or e == "[":
            temp.append(e)
        elif e == ")":
            if not len(temp) or temp[-1] != "(":
                isYes = False
                break
            temp.pop()
        elif e == "]":
            if not len(temp) or temp[-1] != "[":
                isYes = False
                break
            temp.pop()
    if isYes:
        print("yes")
    else:
        print("no")
