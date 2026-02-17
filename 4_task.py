class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)



    def rate_lecture(self, lecturer, course, grades):
        if isinstance(lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grades]
            else:
                lecturer.grades[course] = [grades]
        else:
            return 'Ошибка'

    def the_average_value(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if len(all_grades) == 0:
            return 0
        return round(sum(all_grades) / len(all_grades), 2)





    def __str__(self):
        student = (f"Имя: {self.name}\n"
                   f"Фамилия: {self.surname}\n"
                   f"Средняя оценка за домашние задания: {self.the_average_value()}\n"
                   f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                   f"Завершенные курсы: {', '.join(self.finished_courses)}")
        return student



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self):
        all_grades = []
        for grades_list in self.grades.values():\
                all_grades.extend(grades_list)
        avg_grade = round(sum(all_grades) / len(all_grades), 2)
        if all_grades:
            return avg_grade
        else: 0
        return 0

    def __str__(self):

        some_lecturer = (f"Имя: {self.name}\n"
                         f"Фамилия: {self.surname}\n"
                         f"Средняя оценка за лекции: {self.avg_grade()}")
        return some_lecturer

    def lecturer_vs_student(self):
        student_average_grade = student.the_average_value()
        lecture_average_grade = lecturer.avg_grade()
        if student_average_grade == lecture_average_grade:
            return f'Средняя оценка лекторов и студентов равны. {student_average_grade} = {lecture_average_grade}'
        elif student_average_grade > lecture_average_grade:
            return f'Cредняя оценка студентов выше чем лекторов {student_average_grade} > {lecture_average_grade}'
        else:
            return f'Cредняя оценка лекторов выше чем студентов {student_average_grade} < {lecture_average_grade}'




class Reviewer(Mentor):
    def __init__(self, name, surname):
     super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
             if course in student.grades:
                 student.grades[course] += [grade]
             else:
                 student.grades[course] = [grade]
         else:
             return 'Ошибка'



    def __str__(self):
        some_reviewer = (f"Имя: {self.name}"
                         f"\nФамилия: {self.surname}")
        return some_reviewer



# Созданные лекторы
lecturer = Lecturer('Иван', 'Иванов')
lecturer1 = Lecturer('Николай', 'Сафронов')

# Созданные ревьюверы
reviewer = Reviewer('Пётр', 'Петров')
reviewer1 = Reviewer('Александр', 'Никитко')

# Созданные студенты
student = Student('Ольга', 'Алёхина', 'Ж')
student1 = Student('Иван', 'Смирнов', 'М')


reviewer.rate_hw(student, 'Python', 3)
reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 3)

student.courses_in_progress += ['Python', 'Git']
student.finished_courses += ['Введение в программирование']
student.grades['Python'] = [10, 5, 8, 0]

lecturer.courses_attached += ['Python', 'Git']
reviewer.courses_attached += ['Python', 'Git']

student.rate_lecture(lecturer, 'Python', 7)
student.rate_lecture(lecturer, 'Python', 4)



print('-------------reviewer------------')
print(reviewer)
print('-------------lecturer------------')
print(lecturer)
print('----------student-----------')
print(student)
print('----------Средняя оценка-----------')
print(lecturer.lecturer_vs_student())


def average_student_grade(students, course_name):
    all_grades = []
    for student in students:
        if course_name in student.grades:
            all_grades.extend(student.grades[course_name])
    if all_grades:
        return round(sum(all_grades) / len(all_grades), 2)
    return 0


def average_lecturer_grade(lecturers, course_name):
    all_grades = []
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])
    if all_grades:
        return round(sum(all_grades) / len(all_grades), 2)
    return

print('\n Средняя оценка студентов по курсу Python ')
print(average_student_grade([student, student1], 'Python'))


print('\n Средняя оценка лекторов по курсу Python ')
print(average_lecturer_grade([lecturer, lecturer1], 'Python'))