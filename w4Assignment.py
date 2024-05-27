class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, My name is {self.name}. \nI am {self.age} years old and my gender is {self.gender}")

person1 = Person("Joe", 18, "Male")
person1.introduce()