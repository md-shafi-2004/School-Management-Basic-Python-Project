from classroom import ClassRoom
from student import Student
from teacher import Teacher
from person import Person


class School():  #school is responsible for classroom because classroom's imidiete owner is school
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.classrooms=[]  #one school has many classroom

    def add_classroom(self,classroom):
        self.classrooms.append(classroom)

    def show_classroom(self):   #if we want to know what is in the classroom ,we need to ask school because God knows everything about a person because HE is watching from multiple dimension
        for i in self.classrooms:
            print(f"Classroom name : {i.name}")
            print("Students are :")
            for s in i.students:
                print(f"\t {s.name} {s.roll} {s.age}")
            print("Teachers are:")
            for t in i.teachers:
                print(f"\t {t.name} {t.subject}")
            print("\n")
    