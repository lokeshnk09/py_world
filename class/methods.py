
class Student:

    School = 'SVS'

    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def get_school_info(cls):
        return cls.School

    @staticmethod
    def info():
        return 'Welcome to SVS School'


s1 = Student(52,65,98)
s2 = Student(45,98,79)

av1 = Student.avg(s1)
av2 = Student.avg(s2)

print(av1)
print(av2)
print(Student.get_school_info())
print(Student.info())

