# coding=utf-8
class Person(object):
    def __init__(self, flag=False, name="jim"):
        self.name = name
        self.flag = flag
        print("Person", self.name)

    def call(self):
        print(self.flag, "name:", self.name)
        self.flag = not self.flag


class Programmer(Person):
    def __init__(self, flag=True, name="Dotjar", age=19):
        self.age = 19
        super(Programmer, self).__init__(flag, name)
        print("Programmer's age:", self.age)

    def set_name(self, name):
        self.name = name


coder = Programmer()
coder.call()
coder.set_name("dotjar")
coder.call()
