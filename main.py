import random


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def get_grade(self, grade):
        self.grades.append(grade)

    def is_excellent(self):
        return set(self.grades) == {5}

    def get_name(self):
        return self.name


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


class Parent:
    def __init__(self, mood, *children):
        self.mood = mood
        self.children_list = [*children]

    def average_excellent(self):
        count = 0
        excellent_count = 0

        for c in self.children_list:
            count += 1
            if c.is_excellent():
                excellent_count += 1

            return excellent_count/count

    def say_some_th(self, c):
        if c.is_excellent:
            if self.mood:
                print(c.get_name(), " is nice child")
            else:
                print(c.get_name(), " is nice, but I angry")
        else:
            if self.mood:
                print(c.get_name(), " is ok")
            else:
                print(c.get_name(), " is very stupid guy")

    def say_iter(self):
        for c in self.children_list:
            self.say_some_th(c)

    def say_random(self):
        cur = random.choice(self.children_list)
        self.say_some_th(cur)

    def say_all(self):
        factor = self.average_excellent()

        if factor == 1:
            if self.mood:
                print("My children is nice")
            else:
                print("My children is good")
        elif 0.5 < factor < 1:
            if self.mood:
                print("My children is good")
            else:
                print("My children is OK")
        else:
            if self.mood:
                print("My children is OK")
            else:
                print("My children is terrible")

    def say_one(self, child):
        if not (child in self.children_list):
            raise ValueError("ERROR: Child is not assigment to this parent")
        else:
            self.say_some_th(child)


if __name__ == "__main__":
    # Этап 1
    s1 = Student("Oleg")
    s2 = Student("Ivan")

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

    # Этап 7

    p1 = Parent(True, s1)
    p2 = Parent(False, s1, s2)

    p1.say_random()
    p2.say_all()
    p2.say_iter()
    p1.say_one(s1)

    try:
        p1.say_one(s2)
    except ValueError as e:
        print(e)
