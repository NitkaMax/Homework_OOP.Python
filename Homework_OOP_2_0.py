from __future__ import print_function


def average_number(numbers):
    if numbers:
        if isinstance(numbers, dict):
            res=[]
            for value in numbers.values():
                res += value
            return sum(res)/len(res)
        else:
            return sum(numbers)/len(numbers)
    else:
        return 0

def evaluation(persons, course):
    res = 0
    lenth = 0
    for person in persons:
        if course in person.grades:
            if person.grades[course]:
                res += average_number(person.grades[course])
                lenth += 1
    if lenth != 0:
        return res/lenth

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if isinstance(grade, int) and (0 <= grade <= 10) :
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                print("Оценка введена неверно")
        else:
            return 'Ошибка'
    def __str__(self):
        info = str(f"Имя: {self.name}\n"
                   f"Фамилия: {self.surname}\n"
                   f"Средняя оценка: {average_number(self.grades)}\n"
                   f"Курсы в процессе обучения: {', '.join(self.courses_in_progress)}\n"
                   f"Завершенные курсы: {', '.join(self.finished_courses)}\n")
        return info
    def __lt__(self, other):
        return average_number(self.grades) < average_number(other.grades)
    def __gt__(self, other):
        return average_number(self.grades) > average_number(other.grades)
    def __le__(self, other):
        return average_number(self.grades) <= average_number(other.grades)
    def __ge__(self, other):
        return average_number(self.grades) >= average_number(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {average_number(self.grades)}"
    def __lt__(self, other):
        return average_number(self.grades) < average_number(other.grades)
    def __gt__(self, other):
        return average_number(self.grades) > average_number(other.grades)
    def __le__(self, other):
        return average_number(self.grades) <= average_number(other.grades)
    def __ge__(self, other):
        return average_number(self.grades) >= average_number(other.grades)


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
            

student_list = []

student1 = Student('Артем', 'Попов', 'male')
student1.courses_in_progress += ['Python-разработка для начинающих']
student1.courses_in_progress += ['Git — система контроля версий']
student1.courses_in_progress += ['Java']
student1.finished_courses += ['Основы языка программирования Python']
student2 = Student('Даниил', 'Климов', 'male')
student2.courses_in_progress += ['Python-разработка для начинающих']
student2.courses_in_progress += ['Основы Java Script']
student2.finished_courses += ['Маникюр']
student2.finished_courses += ['Английский для программистов']

student_list.append(student1)
student_list.append(student2)

lecturer_list = []

lecturer1 = Lecturer('Аллен ', 'Барри')
lecturer1.courses_attached += ['Python-разработка для начинающих']
lecturer1.courses_attached += ['Java']
lecturer2 = Lecturer('Хэл', 'Джордан')
lecturer2.courses_attached += ['Основы Java Script']

lecturer_list.append(lecturer1)
lecturer_list.append(lecturer2)

reviewer1 = Reviewer('Кент', 'Кларк')
reviewer1.courses_attached += ['Python-разработка для начинающих']
reviewer1.courses_attached += ['Git — система контроля версий']
reviewer2 = Reviewer('Квин', 'Оливер')
reviewer2.courses_attached += ['Python-разработка для начинающих']
reviewer2.courses_attached += ['Основы Java Script']

reviewer1.rate_hw(student1, 'Python-разработка для начинающих', 8.6)
reviewer1.rate_hw(student1, 'Python-разработка для начинающих', 9.2)
reviewer1.rate_hw(student1, 'Git — система контроля версий', 9.9)
reviewer1.rate_hw(student2, 'Python-разработка для начинающих', 9.4)
reviewer1.rate_hw(student2, 'Python-разработка для начинающих', 6.7)

student1.rate_lecturer(lecturer1, 'Python-разработка для начинающих', 10)
student1.rate_lecturer(lecturer1, 'Python-разработка для начинающих', 9.2)
student1.rate_lecturer(lecturer1, 'Java', 8.2)
student2.rate_lecturer(lecturer1, 'Python-разработка для начинающих', 7.9)
student2.rate_lecturer(lecturer2, 'Основы Java Script', 7.25)
student2.rate_lecturer(lecturer1, 'Java', 7.9)

print(f"Эксперт 1: \n{reviewer1}\n")
print(f"Эксперт 2: \n{reviewer2}")
print()
print(f"Лектор 1:\n{lecturer1}\n")
print(f"Лектор 2:\n{lecturer2}")
print()
print(f"Студент 1:\n{student1}\n")
print(f"Студент 2:\n{student2}")
print()
print("Лектор 1 < Лектор 2 ==>", lecturer1 > lecturer2)
print("Студент 1 > Студент 2 ==>", student1 > student2)
print()
print(f"Средняя оценка домашних работ по Python: {evaluation(student_list, 'Python-разработка для начинающих')}")
print(f"Средняя оценка лекторов по курсу Python: {evaluation(lecturer_list, 'Python-разработка для начинающих')}")
