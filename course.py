class Student:

    # Атрибут класса для хранения ВСЕХ студентов
    all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

        # Автоматически добавляем студента в общий список при создании
        Student.all_students.append(self)

    def rate_lecture(self, lector, course, grade):
        """Метод для занесения оценок лектору"""
        if grade < 0 or grade > 10:
            return 'Оценка должна быть от 1 до 10'

        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course].append(grade)
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):
        """Метод для расчета средней оценки за курс"""
        if not self.grades:
            return 0
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        """Метод для переопрделения str()"""
        cour_progress = ', '.join(map(str, self.courses_in_progress))
        fin_cour = ', '.join(map(str, self.finished_courses))

        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.get_average_grade()}\n'
                f'Курсы в процессе изучения: {cour_progress}\n'
                f'Завершенные курсы: {fin_cour}\n')

    def __eq__(self, other):
        """Метод для сравнения двух экземпляров классов по средней оценке"""
        return self.get_average_grade() == other.get_average_grade()

    def __gt__(self, other):
        """Метод для сравнения двух экземпляров классов по средней оценке"""
        return self.get_average_grade() > other.get_average_grade()

    def __lt__(self, other):
        """Метод для сравнения двух экземпляров классов по средней оценке"""
        return self.get_average_grade() < other.get_average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    # Атрибут класса для хранения ВСЕХ лекторов
    all_lecturer = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

        # Автоматически добавляем лектора в общий список при создании
        Lecturer.all_lecturer.append(self)

    def get_average_grade(self):
        """Метод для расчета средней оценки"""
        if not self.grades:
            return 0
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        """Метод для переопрделения str()"""
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.get_average_grade()}\n')

    def __eq__(self, other):
        """Метод для сравнения двух экземпляров классов по средней оценке"""
        return self.get_average_grade() == other.get_average_grade()

    def __gt__(self, other):
        """Метод для сравнения двух экземпляров классов по средней оценке"""
        return self.get_average_grade() > other.get_average_grade()

    def __lt__(self, other):
        """Метод для сравнения двух экземпляров классов по средней оценке"""
        return self.get_average_grade() < other.get_average_grade()


class Reviewer(Mentor):
    """Метод для занесения оценок эксперту"""
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    """Метод для переопрделения str()"""
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')