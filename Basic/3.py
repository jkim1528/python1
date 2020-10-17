# Library: 다른 사람이 만들어 놓은 클래스를 가져다 쓰는 것.
from datetime import datetime

# class : 일련의 method(명령어)와 변수를 모아놓은 파일
hour = datetime.now().hour
print(hour)

if hour < 12:
    print('am')
if hour >= 12:
    print('pm')

hour = 9
if hour > 12:
    print('pm')
elif hour == 12:
    print('noon')
elif hour == 11:
    print('11')
elif hour == 10:
    print('10')
elif hour == 9:
    print('9')
else:
    print('morning')

# method(parameter) : static 명령어(인풋값) or nonstatice 명령어()
def method1():
    print('method1 started')
def method2():
    print('method2 started')

method1()
method2()

a = 1
b = 3

def add1():
    result = a + b
    print(result)

add1()

def add2(a,b):
    result = a + b
    print(result)

add2(1,3)


def add10(input):
    result = input + 10
    print(result)

add10(5)

def print_round(number):
    result = round(number)
    print(result)

print_round(4.6)
print_round(2.2)

def add3(a,b):
    result = a + b
    print("{} + {} = {}".format(a,b,result))

add3(10,5)
