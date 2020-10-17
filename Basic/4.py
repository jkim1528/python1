# input
# print('input name > ', end = ' ')
# name = input()
# print('Your name is ', name, '.')
# Ctrl + C : Cancel (Powercell)

# list (배열) 변수 : 다수의 index를 갖고 있는 변수, 0부터 시작함에 주의!
list1 = [1,2,3,4,5]
print(list1[0])
print(list1[1])
print(list1[-1])
print(list1[-2])
# print(list1[5]) # error
# print(list1[6]) # error

# 虹色　にじ : あかい、オレンジ、きいろ、みどり、あお、あいいろ、むらさき
rainbow=['red','orange','yellow','green','blue','indigo','purple']
first = rainbow[0]
last = rainbow[-1]
print('first is {}'.format(first))
print('last is {}'.format(last))
print(rainbow)

# listの追加
list2 = [1,2,3]
list2.append(6)
list2.append(10)
print(list2)

list3 = list2+[5]
print(list3)

list3 = list3+[6]
list3 = list3+[6]
list3 = list3+[6]
print(list3)

print(list3[2])

# listの削除
list4 = [1,2,3,4,5,6,7,8,9,10]
del list4[0]
print(list4)
list4.remove(10)
print(list4)

# listとif文
list5=[6,7]
n = 12
if n in list5:
    print('{} exists'.format(n))
else:
    print("{} doesn't exist".format(n))

# for (pattern) in (patterns)
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i)

# range()
# numbers = [0, 1, 2, 3, 4]
for i in range(5):
    print(i+1)

# enumerate() : 열거하다
names = ['Aoki', 'D.Yang']
for i, name in enumerate(names):
    print('No {} : {}'.format(i+1, name))

print(len(names))

rainbow=['red','orange','yellow','green','blue','indigo','purple']
for i in range(len(rainbow)):
    color = rainbow[i]
    print('No {} : {}'.format(i+1, color))

# 이중배열 () tuple {} dictionary [] list
numbers = [(1,2),(10,0),(3,3),(5,7)]
for a,b in numbers:
    if b == 0:
        print("Cannot divided by 0.")
    else:
        print("{} divide {} = {}".format(a,b,a/b))
