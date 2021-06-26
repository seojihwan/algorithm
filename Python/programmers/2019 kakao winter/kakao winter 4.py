import sys
sys.setrecursionlimit(10000)


def solution(k, room_number):
    rooms = dict()

    def findEmptyRoom(rooms, key):
        if key not in rooms:
            rooms[key] = key + 1
            return key
        temp = findEmptyRoom(rooms, rooms[key])
        rooms[key] = temp + 1
        return temp

    answer = []
    for room in room_number:
        answer.append(findEmptyRoom(rooms, room))
    print(rooms)
    return answer


k = 10
# room_number = [1, 3, 4, 1, 3, 1]
room_number = [1, 3, 4, 1, 3, 1]


print(solution(k, room_number))
