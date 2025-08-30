from school import School
from classroom import ClassRoom
from student import Student
from teacher import Teacher

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

#removing student
#c1.remove_student("S002")

#transfering student
school.transfer_student_to_other_classroom(s1,"Jupiter","Pluto")

#school status
school.show_classroom()