# package : 클래스들을 담아놓은 폴더.
# class : 관련된 변수, 메소드들을 모아놓은 집합. 파일(.py)
import math

pi = math.pi
print(pi)

floor = math.floor(2.6)
print(floor)

import datetime

today = datetime.date.today()
print(today)

import random
rainbow=['red','orange','yellow','green','blue','indigo','purple']
choice = random.choice(rainbow)
print(choice)

random.shuffle(rainbow)
print(rainbow)
