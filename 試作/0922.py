class Dog:
    def __init__(self, name):
       self.name = name

class UltraDog(Dog):
    def __init__(self, name, type_):
        super().__init__(name)
        self.type = type_

ud1 = UltraDog("taro", "akita")
print(ud1.name)
print(ud1.type)