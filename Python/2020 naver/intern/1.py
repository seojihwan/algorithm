# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import defaultdict


def dayToNum(day, letter):
    for idx, e in enumerate(letter):
        if e == day:
            return idx


def numToDay(num, letter):
    for idx, e in enumerate(letter):
        if idx == num:
            return e


def solution(S, K):
    letter = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    return numToDay((dayToNum(S, letter) + K) % 7, letter)


s = "Sun"
k = 1
print(solution(s, k))
