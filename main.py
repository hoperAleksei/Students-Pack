class Student:
    def __init__(self):
        self.grades = []

    def get_grade(self, grade):
        self.grades.append(grade)

    def is_excellent(self):
        return set(self.grades) == {5}


class Teacher:
    def __init__(self):
        ...

    def put_grade(self, student, grade):
        student.get_grade(grade)


if __name__ == "__main__":
    # Этап 1
    s1 = Student()
    s2 = Student()

    s1.get_grade(2)
    s1.get_grade(3)
    s1.get_grade(4)

    s2.get_grade(5)
    s2.get_grade(5)
    s2.get_grade(5)

    print(s1.is_excellent(), s2.is_excellent())

    # Этап 2

    t1 = Teacher()
    t2 = Teacher()

    t1.put_grade(s1, 2)
    t1.put_grade(s2, 5)

    t2.put_grade(s1, 5)
    t2.put_grade(s2, 5)
