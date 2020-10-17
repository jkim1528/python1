print("hello world")

# comment : 메모 적어두는 곳
# variables : 변수 = "변하는 수"
identity = 'pencil'
print('I want to write it by',identity,'.')

# 변수의 종류는 크게 두 가지 있음: 숫자와 문자열 변수로 나뉨. 이걸 변수의 data type이라고 함. 정수와 실수, 문자열 data type이라고 함. int, double (or float), string
a = 5
b = 1.1
c = 'hello'

# 숫자 변수는 사칙연산이 가능, 문자 변수는 불가능
a = a+1
b = b+1.9
# c = c+1
# print(a)
# print(b)
# print(c)

a = (a-3)*3/9
print(a)

d = 'world'
print(c,d)

# 데이터타입별 초기화 방법
a = 0
b = 0.0
c = ''

# 제곱, 나머지, 몫
a = 2
a = a ** 5
b = 5
b = b % a
c = 10
c = c // 2
print(a)
print(b)
print(c)

a = '1'
b = '1'
a = a + b
print(a)

# 문자열 3종류
string1 = 'hello kim'
string2 = "hello 'kim'"
string3 = """  "hello" 'kim'
!
 """
print(string1)
print(string2)
print(string3)

# print의 출력형식(format) 3가지
number = 20
name = 'Mr. Kim'
base = 'Welcome, {}. Your room # is {}'

print('Welcome,',name,'. Your room # is',number)
print(base.format(name,number))
print('Welcome, {}. Your room # is {}'.format(name,number))

# casting : 데이터타입을 바꾸는 것
# int : 정수, string : 문자열, float : 실수
a = 1.1
b = 1
c = a + b
c = int(c)
print(c)
c = 2
c = float(c)
print(c)

# datatype
"""
int(integer) 정수 a = 0
float 실수 a = 0.0
string 문자열 a = ''
list 리스트 a = []
dict(dictionary) 딕셔너리 a = {}
bool(boolean) 0,[],Noneは(false)になります。その以外は全部(true)になります。
"""
a = bool(0)    #False
b = bool(3.3)  #True
c = bool([])    #False
d = bool(None)    #False
print(a, b, c, d)

# datatype print
list = [1, 2, 3]
dict = {"pen": 100, "pencilcase": 300}
tuple = (1, 2, 3)
number = 10
real_number = 3.141592

print(type(list))
print(type(dict))
print(type(tuple))
print(type(number))
print(type(real_number))
