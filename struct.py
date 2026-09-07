class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

s = Student("Rahul", 101, 87.5)
print(s.name, s.roll, s.marks)
