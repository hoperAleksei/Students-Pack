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
        self.change = 5
        self.count = 0

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

        self.count += 1
        if self.count == self.change:
            self.mood = bool(random.getrandbits(1))
            self.count = 0

        student.get_grade(grade)


class ConstTeacher(Teacher):
    def __init__(self, mood, const):
        super().__init__(mood)
        self.const = const

    def put_grade(self, student):
        student.get_grade(self.const)


class Lesson:
    def __init__(self, teacher, *students):
        self.teacher = teacher
        self.students_list = [*students]

    def time_to_grade(self):
        grade_count = random.randint(0, len(self.students_list))

        ungraded = self.students_list.copy()
        for i in range(grade_count):
            cur = random.choice(ungraded)
            ungraded.remove(cur)

            self.teacher.put_grade(cur)


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

    # Этап 4

    l1 = Lesson(t1, s1, s2)
    l2 = Lesson(t2, s1, s2)

    print(s1.grades, s2.grades)

    l1.time_to_grade()
    print(s1.grades, s2.grades)

    l2.time_to_grade()
    print(s1.grades, s2.grades)

    # Этап 5, 6

    ct1 = ConstTeacher(True, 5)
    ct2 = ConstTeacher(False, 2)

    l3 = Lesson(ct1, s1, s2)
    l4 = Lesson(ct2, s1, s2)

    print(s1.grades, s2.grades)

    l3.time_to_grade()
    print(s1.grades, s2.grades)

    l4.time_to_grade()
    print(s1.grades, s2.grades)
