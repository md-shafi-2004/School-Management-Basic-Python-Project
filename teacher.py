from person import Person

class Teacher(Person):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject=subject
