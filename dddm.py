# Base class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("----- PERSON DETAILS -----")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Derived class Student (inherits Person)
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student(self):
        print("----- STUDENT DETAILS -----")
        print(f"Course: {self.course}")


# Derived class Exam (inherits Student) – Multilevel Inheritance
class Exam(Student):
    def __init__(self, name, age, course, m1, m2, m3):
        super().__init__(name, age, course)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.total = 0

    def compute_total(self):
        self.total = self.m1 + self.m2 + self.m3

    def display_exam(self):
        print("----- EXAM DETAILS -----")
        print(f"Marks 1: {self.m1}")
        print(f"Marks 2: {self.m2}")
        print(f"Marks 3: {self.m3}")
        print(f"Total Marks: {self.total}")


# Creating an object of Exam class with sample data
exam1 = Exam("shubham chaudhary", 34, "BCA", 85, 90, 88)
exam1.compute_total()

# Display all details
exam1.display_person()
exam1.display_student()
exam1.display_exam()
