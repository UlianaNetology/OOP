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



    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
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
        for grades_list in self.grades.values():
                all_grades.extend(grades_list)
        if all_grades:
            avg_grade = round(sum(all_grades) / len(all_grades), 2)
            return avg_grade
        else:
            return 0


    def __str__(self):

        some_lecturer = (f"Имя: {self.name}\n"
                         f"Фамилия: {self.surname}\n"
                         f"Средняя оценка за лекции: {self.avg_grade()}")
        return some_lecturer

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() < other.the_average_value()
        elif isinstance(other, Lecturer):
            return self.avg_grade() < other.avg_grade()
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() == other.the_average_value()
        elif isinstance(other, Lecturer):
            return self.avg_grade() == other.avg_grade()
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() > other.the_average_value()
        elif isinstance(other, Lecturer):
            return self.avg_grade() > other.avg_grade()
        else:
            return NotImplemented


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

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



lecturer = Lecturer('Some', 'Buddy')
reviewer = Reviewer('Some', 'Buddy')
student = Student('Ruoy', 'Eman', 'М')


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
#print(lecturer.lecturer_vs_student())

print(f'Средняя оценка лекторов({lecturer.avg_grade()}) и студентов({student.the_average_value()}) равны  : {lecturer == student}')
print(f'Cредняя оценка студентов({student.the_average_value()}) выше чем лекторов({lecturer.avg_grade()}): {lecturer < student}')
print(f'Cредняя оценка лекторов({lecturer.avg_grade()}) выше чем студентов({student.the_average_value()}): {lecturer > student}')