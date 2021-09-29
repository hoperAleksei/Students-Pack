import random


class Student:
    def __init__(self):
        self.grades = []

    def get_grade(self, grade):
        self.grades.append(grade)

    def is_excellent(self):
        return set(self.grades) == {5}


class Teacher:
    def __init__(self, mood):
        self.mood = mood  # хорошее насроение = True

    def put_grade(self, student):
        if student.is_excellent():
            if self.mood:
                grade = 5
            else:
                grade = random.randint(4, 5)
        else:
            if self.mood:
                grade = 4
            else:
                grade = random.randint(2, 3)

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

    # Этап 2, 3

    t1 = Teacher(False)
    t2 = Teacher(True)

    t1.put_grade(s1)
    t1.put_grade(s2)

    t2.put_grade(s1)
    t2.put_grade(s2)
