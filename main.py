import random


class Student:
    def __init__(self, name, *parents):
        self.name = name
        self.grades = []
        self.parents = [*parents]

    def get_grade(self, grade):
        self.grades.append(grade)

    def is_excellent(self):
        return set(self.grades) == {5}

    def add_parents(self, *parents):
        self.parents.extend(parents)

    def __str__(self):
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
    def __init__(self, name, teacher, *students):
        self.name = name
        self.teacher = teacher
        self.students_list = [*students]
        self.graded = []

        grade_count = random.randint(0, len(self.students_list))

        ungraded = self.students_list.copy()
        for i in range(grade_count):
            cur = random.choice(ungraded)
            ungraded.remove(cur)

            self.graded.append(cur)

            self.teacher.put_grade(cur)

    def __str__(self):
        return self.name


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
                print(c, " is nice child")
            else:
                print(c, " is nice, but I angry")
        else:
            if self.mood:
                print(c, " is ok")
            else:
                print(c, " is very stupid guy")

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


class Meeting:
    def __init__(self, teachers, parents, lessons):
        self.teachers_list = list(teachers)
        self.parents_list = list(parents)
        self.lessons_list = list(lessons)

    def __call__(self, *args, **kwargs):
        absent = set()
        for les in self.lessons_list:
            print("Lesson: {}".format(les))

            if not (les.teacher in self.teachers_list):
                continue

            for s in les.graded:
                ind = True

                for p in s.parents:
                    if p in self.parents_list:
                        p.say_one(s)

                        ind = False

                if ind:
                    absent.add(s)

        if len(absent) > 0:
            print(*absent, sep=", ", end=" ")
            if len(absent) > 1:
                print("are absent")
            else:
                print("is absent")


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

    print(s1.grades, s2.grades)

    l1 = Lesson("Math", t1, s1, s2)

    print(s1.grades, s2.grades)

    l2 = Lesson("Frontend", t2, s1, s2)

    print(s1.grades, s2.grades)

    # l1.time_to_grade()
    # print(s1.grades, s2.grades)
    #
    # l2.time_to_grade()
    # print(s1.grades, s2.grades)

    # Этап 5, 6

    ct1 = ConstTeacher(True, 5)
    ct2 = ConstTeacher(False, 2)

    print(s1.grades, s2.grades)

    l3 = Lesson("Backend", ct1, s1, s2)

    print(s1.grades, s2.grades)

    l4 = Lesson("Lecture", ct2, s1, s2)

    print(s1.grades, s2.grades)

    # l3.time_to_grade()
    # print(s1.grades, s2.grades)
    #
    # l4.time_to_grade()
    # print(s1.grades, s2.grades)

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

    # Этап 8

    s1.add_parents(p1, p2)
    s2.add_parents(p2)

    m1 = Meeting((t1, t2, ct1, ct2), (p1, p2), (l1, l2, l3, l4))

    m2 = Meeting((t1, t2, ct1, ct2), (p1, ), (l1, l2, l3, l4))

    m3 = Meeting((t1, t2, ct1, ct2), (p2, ), (l1, l2, l3, l4))

    m4 = Meeting((t1, ), (p1, p2), (l1, l2, l3, l4))

    m1()
    m2()
    m3()
    m4()
