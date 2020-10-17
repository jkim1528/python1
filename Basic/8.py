class Animal(): # 親クラス
    def walk(self):
        print("Walking")
    def eat(self):
        print("Eating")
    def greet(self):
        print("Greeting")

class Human(Animal): # Animal()の子息クラス1、だからparameterはAnimalしかもらえない。
    def walk(self):
        print("Walking")
    def eat(self):
        print("Eating")
    def wave(self):
        print("Wave hand") # ふります。흔들다
    def greet(self): # Animal()の中にあるgreet(self)をoverrideする。
        self.wave()

class Dog(Animal): # Animal()の子息クラス2、だからparameterはAnimalしかもらえない。
    def walk(self):
        print("Walking")
    def eat(self):
        print("Eating")
    def wag(self):
        print("Wave tails") #　しっぽ 꼬리
    def greet(self): # Animal()の中にあるgreet(self)をoverrideする。
        self.wag()

human1 = Human()
dog1 = Dog()

# Instance로 쓰지 않고 아래와 같이만 쓸 경우에는 self parameter가 필요 없다.
# Animal.greet()
# Human.greet()

# self parameter는 그 method를 호출하는 instance가 해당 class의 복제본이라는 것을 의미한다.

# 別な事がoverrideされていますから、humanとdogは挨拶する方法が違うになる。
human1.greet()
dog1.greet()

# humanとdogは親クラスがanimalで、同じだから、walkとeatの方法がanimal方と同じだ。
human1.walk()
dog1.walk()
human1.eat()
dog1.eat()
