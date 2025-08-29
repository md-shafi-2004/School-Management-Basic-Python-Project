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

    def remove_student(self,roll):
        student=self.find_student(roll)
        if student:
            self.students.remove(student)
        else:
            print(f"{roll} is not a student of this school")
            
    def find_student(self,roll):  #classroom is responsible for student that is why find_student is here
        for student in self.students:
            if student.roll==roll:
                return student
        else:
            return None

