class Student:

    '''Создает студентов'''

    def __init__(self, name, surname, gender):

        '''Конструктор класса Student.
        Добавляет студента и определяет его атрибуты'''

        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {} 

    def rate_hw(self, lecture, course, grade):

        '''Метод добавляет оценку лектору за предоставленный курс при условии,
что лектор является объктом класса Lecture, предоставленный курс закреплен за
указанным лектором и данный курс входит в список курсов текущего студента'''
        
        if (isinstance(lecture, Lecture) and
            course in lecture.courses_attached and
            course in self.courses_in_progress):
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return f'Error for {lecture.name} {lecture.surname}'
 
class Mentor:

    '''Создает учителей'''

    def __init__(self, name, surname):

        '''Конструктор класса Mentor.
        Добавляет учителя и определяет его атрибуты'''

        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecture(Mentor):

    '''Создает учителей-лекторов'''

    def __init__(self, name, surname):

        '''Конструктор класса Lecture.
        Добавляет лектора и определяет его атрибуты'''

        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):

    '''Создает учителей-экспертов, проверяющих домашние задания'''

    def rate_hw(self, student, course, grade):

        '''Метод добавляет оценку студенту за пройденный курс при условии,
что студент является объктом класса Student, пройденный курс закреплен за
текущим учителем и данный курс входит в список курсов указанного студента'''
        
        if (isinstance(student, Student) and
            course in self.courses_attached and
            course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка' 

best_student = Student('Ruoy', 'Eman', 'man')
best_student.courses_in_progress += ['Python', 'Java']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecture = Lecture('Irina', 'Shayk')
cool_lecture.courses_attached += ['Python', 'Java', 'C++']

best_student.rate_hw(cool_lecture, 'Python', 9)
best_student.rate_hw(cool_lecture, 'Python', 6)
best_student.rate_hw(cool_lecture, 'Python', 9)
print(best_student.rate_hw(cool_lecture, 'Java', 1))
print(best_student.rate_hw(cool_lecture, 'C++', 5))

print(best_student.rate_hw(cool_reviewer, 'Python', 3))
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)
print(best_student.__dict__)
print(cool_lecture.__dict__)
print(cool_reviewer.__dict__)
