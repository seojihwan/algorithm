class Hashtable:
    def __init__(self):
        self.table = [[] for _ in range(100000)]

    def hash(self, data):
        sum = 0
        for letter in data:
            sum += sum * 7 + ord(letter)
        return sum % len(self.table)

    def insert(self, data):
        self.table[self.hash(data)].append(data)

    def search(self, data):
        temp = self.hash(data)
        for i in range(len(self.table[temp])):
            if self.table[temp][i] == data:
                return True
        return False


n = int(input())
k = int(input())

test = Hashtable()

i_word = input().split()

r_word = input().split()
print(len(i_word))
print(len(r_word))

for num in range(n):
    test.insert(i_word[num])
for j in range(k):
    if not test.search(r_word[j]):
        print(0)
        break
    elif j == k-1:
        print(1)
