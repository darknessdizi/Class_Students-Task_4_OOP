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

    def __str__(self):
        name = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        text = f'Средняя оценка за лекции: {self.__average_rating()}'
        return name + text

    def __average_rating(self):
        count = 0
        total_length = 0
        for key, value in self.grades.items():
            count += sum(value)
            total_length += len(value)
        if total_length == 0:
            return 'Нет оценок'
        return round(count/total_length, 1)

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

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

best_student = Student('Ruoy', 'Eman', 'man')
best_student.courses_in_progress += ['Python', 'Java']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecture = Lecture('Irina', 'Shayk')
cool_lecture.courses_attached += ['Python', 'Java', 'C++']
cool_lecture_2 = Lecture('Baks', 'Banny')
cool_lecture_2.courses_attached += ['Python', 'Java', 'C++', 'Html']

best_student.rate_hw(cool_lecture, 'Python', 9)
best_student.rate_hw(cool_lecture, 'Python', 6)
best_student.rate_hw(cool_lecture, 'Python', 9)
print(best_student.rate_hw(cool_lecture, 'Java', 3))
print(best_student.rate_hw(cool_lecture, 'C++', 5))

print(best_student.rate_hw(cool_reviewer, 'Python', 3))
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)
print(best_student.__dict__)
print(cool_lecture.__dict__)
print(cool_reviewer.__dict__)
print(cool_lecture_2.__dict__)
print(best_student)
print(cool_reviewer)
print(cool_lecture)
print(cool_lecture_2)
