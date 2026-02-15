from course import *


"""Задание № 1. Наследование"""
print()
print("Задание № 1. Наследование")

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []

"""Задание № 2. Атрибуты и взаимодействие классов"""
print()
print("Задание № 2. Атрибуты и взаимодействие классов")
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java', 'C++']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка
print(student.rate_lecture(lecturer, 'Python', 2))  # None

print(lecturer.grades)  # {'Python': [7]}
print(student.rate_lecture(lecturer, 'C++', 3))
print(student.rate_lecture(lecturer, 'C++', 4))


"""Задание № 3. Полиморфизм и магические методы"""
print()
print("Задание № 3. Полиморфизм и магические методы")
print(str(reviewer))
print(str(lecturer))
student.finished_courses += ['Введение в программирование']
student.grades['Python'] = [5]
student.grades['Git'] = [3]

print(student.grades)
print(str(student))

print(lecturer == student)
print(student == lecturer)

"""Задание № 4. Полевые испытания"""
print()
print("Задание № 4. Полевые испытания")
lecturer1 = Lecturer('Василий', 'Заплутанов')
lecturer2 = Lecturer('Ольга', 'Дунаева')
reviewer1 = Reviewer('Андрей', 'Петров')
reviewer2 = Reviewer('Анастасия', 'Стерхова')
student1 = Student('Анна', 'Панькова', 'Ж')
student2 = Student('Александр', 'Акимов', 'М')

lecturer1.courses_attached += ['Python', 'C++', 'Git']
lecturer2.courses_attached += ['Java', 'Git']
reviewer1.courses_attached += ['Python', 'C++']
reviewer2.courses_attached += ['Java', 'Git']
student1.courses_in_progress += ['Python', 'C++', 'Git']
student2.courses_in_progress += ['Python', 'Java', 'Git']
student1.finished_courses += ['Введение в программирование']
student2.finished_courses += ['Введение в программирование']
student1.grades['Python'] = [5, 4, 5]
student1.grades['C++'] = [3]
student2.grades['Java'] = [3, 2, 4]
student2.grades['Git'] = [5, 1]
student2.grades['Python'] = [3, 4, 2]

print(student1.grades)
print(student2.grades)

student1.rate_lecture(lecturer1, 'Python', 2)
student1.rate_lecture(lecturer2, 'Git', 5)
student2.rate_lecture(lecturer1, 'Python', 4)
student2.rate_lecture(lecturer2, 'Git', 3)
student1.rate_lecture(lecturer1, 'Git', 3)
student2.rate_lecture(lecturer1, 'Git', 4)

print()
print(lecturer1.grades)
print(lecturer2.grades)
print()
print(str(lecturer1))
print(str(lecturer2))
print()
print(str(reviewer1))
print(str(reviewer2))
print()
print(str(student1))
print(str(student2))
print()
print(lecturer1 == student2)
print(student1 == lecturer2)

# Передаем название курса и список студентов:
course_input = 'Python'
student_input = [
    {'name': 'Анна', 'surname': 'Панькова'},
    {'name': 'Александр', 'surname': 'Акимов'},
]


def get_student_grades(name, surname, course):
    """Функция для получения оценок студента"""
    for student in Student.all_students:
        if student.name == name and student.surname == surname:
            if course in student.grades:
                return student.grades[course]
            return []  # Пустой список, если нет оценок
    return []  # Пустой список, если студент не найден


def get_stud_grades(students, course):
    """Функция для получения средней оценки за домашнее задание у списка студентов"""
    grade_list = []

    for stud in students:
        grades = get_student_grades(stud['name'], stud['surname'], course)
        if grades:  # Проверяем, что список не пустой
            grade_list.extend(grades)

    if not grade_list:
        return 0

    return sum(grade_list) / len(grade_list)

print(f'Средняя оценка за домашние задания: {get_stud_grades(student_input, course_input)}')

# Передаем название курса и список лекторов:
course_input = 'Git'
lectur_input = [
    {'name': 'Василий', 'surname': 'Заплутанов'},
    {'name': 'Ольга', 'surname': 'Дунаева'},
]


def get_lecturer_grades(name, surname, course):
    """Функция для получения оценок лектора"""
    for lect in Lecturer.all_lecturer:
        if lect.name == name and lect.surname == surname:
            if course in lect.grades:
                return lect.grades[course]
            return []  # Пустой список, если нет оценок
    return []  # Пустой список, если лектор не найден


def get_lect_grades(lecturers, course):
    """Функция для получения средней оценки за курс у лектора"""
    grade_list = []

    for lect in lecturers:
        grades = get_lecturer_grades(lect['name'], lect['surname'], course)
        if grades:  # Проверяем, что список не пустой
            grade_list.extend(grades)

    if not grade_list:
        return 0

    return sum(grade_list) / len(grade_list)

print(f'Средняя оценка лекторов за курс: {get_lect_grades(lectur_input, course_input)}')