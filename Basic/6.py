# 반복문 : for 지정된 구간동안 계속된다. while 조건이 충족되는 한 반복.

# length
numbers = [1,2,3]
length = len(numbers)
i = 0
while i<length:
    print(numbers[i])
    i = i + 1

# break
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for val in list:
    if val % 3 == 0:
        print(val)
        break

sizes = [33,35,34,37,32,35,39,32,35,29,32]
for i, size in enumerate(sizes):
    if size == 32:
        print("32 size is in the {}th size.".format(i+1))
        break

# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
