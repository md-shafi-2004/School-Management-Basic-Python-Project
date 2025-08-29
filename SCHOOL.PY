class School():  #school is responsible for classroom because classroom's imidiete owner is school
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.classrooms=[]  #one school has many classroom

    def add_classroom(self,classroom):
        self.classrooms.append(classroom)

    def show_classroom(self):   #if we want to know what is in the classroom ,we need to ask school because God knows everything about a person because HE is watching from multiple dimension
        for i in self.classrooms:
            print(f"Classroom name : {i.name}\n")
            print("Students are :")
            for s in i.students:
                print(f"\t {s.name} {s.roll} {s.age}")
            print("Teachers are:")
            for t in i.teachers:
                print(f"\t {t.name} {t.subject}")

    
class ClassRoom():#classroom is responsible for student and teacher because both imidiete owner is classroom
    def __init__(self,name,capasity):
        self.name=name
        self.capasity=capasity
        self.students=[]    #in a classroom we have many students and teachers
        self.teachers=[]

    def assign_teacher(self,teacher):
        self.teachers.append(teacher)

    def add_student(self,student):
        if self.capasity>len(self.students):
            self.students.append(student)
        else:
            print(f"Student capasity excceed for classroom : {self.name}")

class Person():
    def __init__(self,name):
        self.name=name

class Student(Person):
    def __init__(self, name,roll,age):
        super().__init__(name)
        self.roll=roll
        self.age=age

class Teacher(Person):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject=subject


#create school    
school=School("RBA","Allardarga")

#create classroom
c1=ClassRoom("Jupiter",100)
c2=ClassRoom("Nepsunr",50)
c3=ClassRoom("Pluto",40)

#add classrooms in school
school.add_classroom(c1)
school.add_classroom(c2)
school.add_classroom(c3)

#create student
s1=Student("Shafi","S001",20)
s2=Student("Rafi","S002",21)
s3=Student("Kafi","S003",22)
s4=Student("Mafi","S004",20)

#add students in classroom
c1.add_student(s1)
c1.add_student(s2)
c2.add_student(s3)
c3.add_student(s4)

#create teacher
t1=Teacher("Abul","Bangla")
t2=Teacher("Kabul","English")
t3=Teacher("Babul","Ict")
t4=Teacher("Khabul","Math")

#add teachers in classroom
c1.assign_teacher(t1)
c1.assign_teacher(t2)
c2.assign_teacher(t3)
c3.assign_teacher(t4)


#school status
school.show_classroom()