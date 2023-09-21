
class Students:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def sayhello(self):
        print("My name is", self.name, "I'm", self.age, "years", self.gender)


myobje = Students("Tiffany", "Male", 20)
myobje = Students("Vasyl", "Male", 30)
myobje = Students("Evans", "Male", 40)
myobje = Students("Shantele", "Female", 50)
myobje.sayhello()
