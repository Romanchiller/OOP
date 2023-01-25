class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def rate_teachers(self, lector, course, grade):
        if 1 <= grade <= 10 == False:
            return print("Ошибка")
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        sum_list = []
        for grades in self.grades.values():
            sum_list += grades
        res_list = sum(sum_list)
        average_grade = float(res_list / len(sum_list))
        return average_grade

    def __str__(self):
        res = f"Имя:  {self.name} \nФамилия: {self.surname} \nCредняя оценка за домашние задания: {self.average_grade()} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}"
        return res

    def __lt__(self, other):
        if isinstance(other, Student):
            if self.average_grade() < other.average_grade():
                return print(
                    f"Все верно, средняя оценка {self.name} {self.surname} меньше чем средняя оценка{other.name} {other.surname}")
            if self.average_grade() >= other.average_grade():
                return print("Сравнение неверно")
        else:
            print("Cравнение невозможно")

    def __gt__(self, other):
        if isinstance(other, Student):
            if self.average_grade() > other.average_grade():
                return print(
                    f"Все верно, средняя оценка {self.name} {self.surname} больше, чем средняя оценка{other.name} {other.surname}")
            if self.average_grade() <= other.average_grade():
                return print("Сравнение неверно")
        else:
            print("Cравнение невозможно")

    def __eq__(self, other):
        if isinstance(other, Student):
            if self.average_grade() == other.average_grade():
                return print(
                    f"Все верно, средняя оценка {self.name} {self.surname} такая же, как средняя оценка{other.name} {other.surname}")
            if self.average_grade() > other.average_grade():
                return print(
                    f" Средняя оценка {self.name} {self.surname} больше, чем средняя оценка{other.name} {other.surname}")
            if self.average_grade() < other.average_grade():
                return print(
                    f"Средняя оценка {self.name} {self.surname} меньше, чем средняя оценка{other.name} {other.surname}")
        else:
            print("Cравнение невозможно")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lector_list.append(self)

    def average_grade(self):
        sum_list = []
        for grades in self.grades.values():
            sum_list += grades
        res_list = sum(sum_list)
        average_grade = float(res_list / len(sum_list))
        return average_grade

    def __str__(self):
        res = f"Имя:  {self.name} \nФамилия: {self.surname} \nCредняя оценка за лекции: {self.average_grade()}"
        return res

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if self.average_grade() < other.average_grade():
                return print(
                f"Все верно, средняя оценка {self.name} {self.surname} меньше чем средняя оценка{other.name} {other.surname}")
            if self.average_grade() >= other.average_grade():
                return print("Сравнение неверно")
        else:
            print("Cравнение невозможно")

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            if self.average_grade() > other.average_grade():
                return print(
                f"Все верно, средняя оценка {self.name} {self.surname} больше, чем средняя оценка{other.name} {other.surname}")
            if self.average_grade() <= other.average_grade():
                return print("Сравнение неверно")
        else: print("Cравнение невозможно")

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            if self.average_grade() == other.average_grade():
                return print(
                f"Все верно, средняя оценка {self.name} {self.surname} такая же, как средняя оценка{other.name} {other.surname}")
            if self.average_grade() > other.average_grade():
                return print(
                f" Средняя оценка {self.name} {self.surname} больше, чем средняя оценка{other.name} {other.surname}")
            if self.average_grade() < other.average_grade():
                return print(
                f"Средняя оценка {self.name} {self.surname} меньше, чем средняя оценка{other.name} {other.surname}")
        else:
            print("Cравнение невозможно")

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя:  {self.name} \nФамилия: {self.surname}"
        return res


def comparison(lector_x, lector_y):
    if isinstance(lector_1, Lecturer) and isinstance(lector_2, Lecturer):
        if lector_1.average_grade() > lector_2.average_grade():
            return print(f"{lector_1.name} {lector_1.surname} круче чем {lector_2.name} {lector_2.surname}")
        if lector_2.average_grade() > lector_1.average_grade():
            return print(f"{lector_2.name} {lector_2.surname} круче чем {lector_1.name} {lector_1.surname}")
        else:
            return print("Эти преподаватели одинаково круты")
    else:
        return print("Ошибка")


def global_grade_course(list_student, course):
    x = []
    for obj in list_student:
        for el in obj.grades[course]:
            x.append(el)
    res = float(sum(x) / len(x))
    if isinstance(obj, Student):
        return print(f"Средняя оценка по всем студентам за курс {course} : {res}")
    if isinstance(obj, Lecturer):
        return print(f"Средняя оценка по всем лекторам за курс {course} : {res}")


students_list = []
lector_list = []

student_1 = Student('Ivan', 'Ivanov', 'm')
student_1.courses_in_progress += ['Python be', 'История ВЛКСМ', 'Маркс и Энгельс, кто они?']
student_1.finished_courses += ['Python fe']
student_2 = Student('Anna', 'Sudoplatova', 'f')
student_2.courses_in_progress += ['Python fe', 'Маркс и Энгельс, кто они?', 'Python be', 'История ВЛКСМ']
student_2.finished_courses += ['История ВЛКСМ']

lector_1 = Lecturer('Petr', 'Petrov')
lector_1.courses_attached += ['История ВЛКСМ', 'Python be']
lector_2 = Lecturer('Zoya', 'Kosmodemyanskaya')
lector_2.courses_attached += ['Маркс и Энгельс, кто они?', 'Python fe', 'История ВЛКСМ']

reviewer_1 = Reviewer('Vladimir', 'Lenin')
reviewer_1.courses_attached += ['Маркс и Энгельс, кто они?', 'Python be']
reviewer_2 = Reviewer('Iosif', 'Stalin')
reviewer_2.courses_attached += ['История ВЛКСМ', 'Python fe', 'Python be']

reviewer_1.rate_hw(student_1, 'Python be', 7)
reviewer_2.rate_hw(student_1, 'История ВЛКСМ', 5)

reviewer_2.rate_hw(student_2, 'Python fe', 3)
reviewer_1.rate_hw(student_2, 'Маркс и Энгельс, кто они?', 6)
reviewer_2.rate_hw(student_2, 'Python be', 4)
reviewer_2.rate_hw(student_1, 'Python be', 9)

student_1.rate_teachers(lector_1, 'История ВЛКСМ', 4)
student_1.rate_teachers(lector_1, 'Python be', 5)
student_1.rate_teachers(lector_2, 'Маркс и Энгельс, кто они?', 2)

student_2.rate_teachers(lector_2, 'Python fe', 5)
student_2.rate_teachers(lector_2, 'Маркс и Энгельс, кто они?', 8)
student_2.rate_teachers(lector_1, 'Python be', 1)
student_2.rate_teachers(lector_2, 'История ВЛКСМ', 7)

comparison(lector_1, lector_2)

global_grade_course(students_list, 'Python be')
global_grade_course(lector_list, 'История ВЛКСМ')

print(student_1)
print(student_2)
print(lector_1)
print(lector_2)
print(reviewer_1)
print(reviewer_2)

student_2 < student_1
student_1 > student_2
student_2 == student_1

lector_2 > lector_1
lector_2 < lector_1
lector_1 == lector_2

lector_1 == student_2

lector_1 == student_2
