import random
import os
os.system('cls')

N = int(input("Введите количество кустов на вашей любимой грядке: "))
# N = 9
min = 1
max = 10
countTotal = 0
harvest = max/2*N
bushes = [] # кусты
for bush in range(min,N):
    count = random.randint(min,max)
    bushes.append(count)
    countTotal+= count
if countTotal>harvest:
    print(f"Кусты: {bushes} урожайный нынче год выдался :)")
else:
    print(f"Кусты: {bushes} худовато нынче :(")
print("Пойдем собирать...")
index = 0
countOnBush = 0
maxOnBush = 0
while index< len(bushes):
    # print(bushes[count])
    if index == 0:
        countOnBush = bushes[-1] + bushes[index] + bushes[index+1]
    elif index == len(bushes)-1:
        countOnBush = bushes[0] + bushes[index] + bushes[index-1]
    else:
        countOnBush = bushes[index-1] + bushes[index] + bushes[index+1]
    index+=1
    if countOnBush > maxOnBush:
        maxOnBush = countOnBush
print(f"Максимум с трех кустов: {maxOnBush}")