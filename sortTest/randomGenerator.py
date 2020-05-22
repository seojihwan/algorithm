import random
import sys

# 랜덤 데이터를 만들기 위한 randomGenerator.py 코드입니다.
# 실행하면 데이터 크기 10000, 50000, 100000, 500000, 1000000에 대하여 txt파일을 생성합니다.
input_size = 10000
f = open("./10000.txt", 'w')
f.write(str(input_size) + '\n')
for i in range(input_size):
    data = random.randint(1, sys.maxsize)  # sys.maxsize = 9223372036854775807
    f.write(str(data) + ' ')
f.close()

input_size = 50000
f = open("./50000.txt", 'w')
f.write(str(input_size) + '\n')
for i in range(input_size):
    data = random.randint(1, sys.maxsize)  # sys.maxsize = 9223372036854775807
    f.write(str(data) + ' ')
f.close()

input_size = 100000
f = open("./100000.txt", 'w')
f.write(str(input_size) + '\n')
for i in range(input_size):
    data = random.randint(1, sys.maxsize)  # sys.maxsize = 9223372036854775807
    f.write(str(data) + ' ')
f.close()

input_size = 500000
f = open("./500000.txt", 'w')
f.write(str(input_size) + '\n')
for i in range(input_size):
    data = random.randint(1, sys.maxsize)  # sys.maxsize = 9223372036854775807
    f.write(str(data) + ' ')
f.close()

input_size = 1000000
f = open("./1000000.txt", 'w')
f.write(str(input_size) + '\n')
for i in range(input_size):
    data = random.randint(1, sys.maxsize)  # sys.maxsize = 9223372036854775807
    f.write(str(data) + ' ')
f.close()

input_size = 5000000
f = open("./5000000.txt", 'w')
f.write(str(input_size) + '\n')
for i in range(input_size):
    data = random.randint(1, sys.maxsize)  # sys.maxsize = 9223372036854775807
    f.write(str(data) + ' ')
f.close()
