class Studnets:

    students_nr  = 0

    def __init__(self, grade):
        self.grade = grade
        Studnets.students_nr += 1


student1 = Studnets(3)
print(Studnets.students_nr)
print(Studnets.grade)

student2 = Studnets(5)
print(Studnets.students_nr)
print(Studnets.grade)

