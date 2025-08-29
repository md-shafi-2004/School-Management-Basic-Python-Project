from person import Person

class Student(Person):
    def __init__(self, name,roll,age):
        super().__init__(name)
        self.roll=roll
        self.age=age