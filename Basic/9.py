# class : 関数や変数などのグループ。今のは変数のクラス。
class Human():
    '''人間'''
person1 = Human()
person2 = Human()
person1.language = '日本語'
person2.language = 'English'

class Car():
    '''車'''
taxi = Car()
bus = Car()
mycar = Car()
mycar.name = 'Toyota' # mycar.nameに'Toyota'という値打ちを入れました。
mycar.price = '400万円'
print(mycar.name) # Toyota

class Human():
    # def create(name, weight):
    #     person = Human()
    #     person.name = name
    #     person.weight = weight
    #     return person
    def __init__(self, name, weight): # initialization = 초기화 = 설정 통일 = 인터페이스
        self.name = name
        self.weight = weight

    def __str__(self): # string
        return "{} weighs {}kg".format(self.name, self.weight)

    def eat(self):      # self = メソッドの第一因子(いんし=parameter)
        self.weight += 1      # self.weight = self.weight + 0.1
        print("{} weighs {}kg".format(self.name, self.weight))

    def diet(self):
        self.weight -= 1      # self.weight = self.weight - 0.1
        print("{} weighs {}kg".format(self.name, self.weight))

# person1 = Human.create("ヤンさん", 69)
# person2 = Human.create("青木さん", 54)
person1 = Human("yang", 69)
person2 = Human("aoki", 54)

person1.eat()
person2.diet()

print(person1)
print(person2)

# super() : 上の事の実務Levelの使う方。= super().親クラス
class Animal():
    def __init__(self, name):
        self.name = name

class Human(Animal):
    def __init__(self, name, hand, language):
        super().__init__(name) # 親クラスの"__init__"のmethodを呼出し(よびだし 호출)、自分のclassじゃないからselfは要らない。
        self.hand = hand
        self.lauguage = language

    def __str__(self):
        return "My name is {}. {}-handed person. Main language is {}".format(self.name, self.hand, self.lauguage)

    def introduce(self):
        print("My name is {}. {}-handed person. Main language is {}".format(self.name, self.hand, self.lauguage)) #　しっぽ 꼬리

person1 = Human("Yang", "Right", "Japanese")
person1.introduce()
print(person1)
