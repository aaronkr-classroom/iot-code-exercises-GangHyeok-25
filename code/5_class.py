# 5_class.py

class Animal:
    def__init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"My name is {self.name}!")
    
    def setName(self): # 재정의
        """
        Set the Animal class's name.
        Animal 클래스의 이름 재정의
        :param name: 새로운 Animal의 이름
        """
        self.name = name
        
    def getName(self, name): # 속성 변환
        """
        Return the Animal class's name.
        Animal 클래스의 이름 반환
        :return: Animal의 이름
        """
        return self.name

class Dog(Animal): # 관계
    def_init_(self, name, age = 3):
        super(),__init__(name)
        self.age = age # 속성을 갖는다.
    
    def speak(self):
        print(f"{self.name} says woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow!")
        
# 호출
my_dog = Dog("Spot")
my_cat = Cat("Kit")
my_dog.speak()
my_cat.speak()