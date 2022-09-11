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
            return print(f'Error for {lecture.name} {lecture.surname} от student {self.name}')

    def __str__(self):

        '''Выводит на печать имя, фамилию и среднюю оценку за домашние задания, а так же 
        курсы в процессе и завершенные курсы объекта (для расчетов оценки используется 
        скрытый метод __average_rating)'''

        name = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        average = f'Средняя оценка за домашние задания: {self.__average_rating()}\n'
        courses_in_progress = ', '.join(self.courses_in_progress)
        courses_in_progress = f'Курсы в процессе изучения: {courses_in_progress}\n'
        finished_courses = ', '.join(self.finished_courses)
        finished_courses = f'Завершенные курсы: {finished_courses}'
        return name + average + courses_in_progress + finished_courses

    def __average_rating(self):

        '''Вычисляет среднюю оценку за домашние задания всех предметов'''

        count = 0
        total_length = 0
        for value in self.grades.values():
            count += sum(value)
            total_length += len(value)
        if total_length == 0:
            return 'Нет оценок'
        return round(count/total_length, 1)

    def __lt__(self, second_student):

        '''Метод для оператора меньше'''

        if not isinstance(second_student, Student):
            print('Not a Student!')
            return
        if self.__average_rating() < second_student.__average_rating():
            print(f'True. {self.name} слабее {second_student.name}')
        else:
            print(f'False. {self.name} сильнее {second_student.name}')
            
    def __eq__(self, second_student):

        '''Метод для оператора равенство'''

        if not isinstance(second_student, Student):
            print('Not a Student!')
            return
        if self.__average_rating() == second_student.__average_rating():
            print(f'True. {self.name} и {second_student.name} одинаково умны')
        else:
            print(f'False. {self.name} и {second_student.name} разные')


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

        '''Выводит на печать имя, фамилию и среднюю оценку за лекции
        (для расчетов оценки используется скрытый метод __average_rating)'''

        name = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        average = f'Средняя оценка за лекции: {self.__average_rating()}'
        return name + average

    def __average_rating(self):

        '''Вычисляет среднюю оценку за лекции по всем предметам'''

        count = 0
        total_length = 0
        for value in self.grades.values():
            count += sum(value)
            total_length += len(value)
        if total_length == 0:
            return 'Нет оценок'
        return round(count/total_length, 1)
    
    def __lt__(self, second_lecture):

        '''Метод для оператора меньше'''

        if not isinstance(second_lecture, Lecture):
            print('Not a Lecture!')
            return
        if self.__average_rating() < second_lecture.__average_rating():
            print(f'True. {self.name} слабее {second_lecture.name}')
        else:
            print(f'False. {self.name} сильнее {second_lecture.name}')
            
    def __eq__(self, second_lecture):

        '''Метод для оператора равенство'''
        
        if not isinstance(second_lecture, Lecture):
            print('Not a Lecture!')
            return
        if self.__average_rating() == second_lecture.__average_rating():
            print(f'True. {self.name} и {second_lecture.name} одинаково умны')
        else:
            print(f'False. {self.name} и {second_lecture.name} разные')


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
            return print(f'Ошибка от reviewer {self.name}')

    def __str__(self):

        '''Выводит на печать имя и фамилию объекта класса'''

        return f'Имя: {self.name}\nФамилия: {self.surname}'


def __average_score(list_object, course):
    
    '''Функция подсчитывает средний бал за указанный курс'''

    score = 0
    count = 0
    for object in list_object:
        if course in object.grades:
            score += sum(object.grades[course])/len(object.grades[course])
            count += 1
    return score, count

def assessment_of_homework(list_student, course):

    '''Функция подсчитывает средний бал студентов за указанный курс'''

    score, count = __average_score(list_student, course)
    if count == 0:
        return f'На курсе "{course}" студенты не получили оценок'
    else:
        score = score/count
        return f'Средняя оценка за домашнее задание по "{course}": {score}'

def assessment_for_lectures(list_lecture, course):

    '''Функция подсчитывает средний бал за лекции преподователей по указанному курсу'''

    score, count = __average_score(list_lecture, course)
    if count == 0:
        return f'За курс "{course}" студенты не поставили оценок'
    else:
        score = score/count
        return f'Средняя оценка за лекции по "{course}": {score}'


list_student = []
list_lecture = []

student_1 = Student('Ruoy', 'Eman', 'man')
student_1.courses_in_progress += ['Python', 'Java']
student_1.finished_courses += ['C++']
list_student.append(student_1)

student_2 = Student('Mila', 'Rem', 'woman')
student_2.courses_in_progress += ['Python', 'C++']
list_student.append(student_2)

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Bob', 'Miller')
reviewer_2.courses_attached += ['Java', 'C++']

lecture_1 = Lecture('Irina', 'Shayk')
lecture_1.courses_attached += ['Python', 'Java', 'C++']
list_lecture.append(lecture_1)

lecture_2 = Lecture('Baks', 'Banny')
lecture_2.courses_attached += ['Python', 'Java', 'C++', 'Httml']
list_lecture.append(lecture_2)

lecture_3 = Lecture('Robbi', 'Vilyams')
lecture_3.courses_attached += ['Java', 'C++', 'Httml']
list_lecture.append(lecture_3)

student_2.rate_hw(lecture_1, 'Python', 8)
student_2.rate_hw(lecture_2, 'Python', 9)
student_2.rate_hw(lecture_1, 'Python', 5)
student_2.rate_hw(lecture_1, 'Java', 8)
student_2.rate_hw(lecture_1, 'C++', 7)
student_2.rate_hw(lecture_2, 'Java', 6)

student_1.rate_hw(lecture_1, 'Python', 9)
student_1.rate_hw(lecture_1, 'Python', 6)
student_1.rate_hw(lecture_1, 'Python', 9)
student_1.rate_hw(lecture_1, 'Java', 3)
student_1.rate_hw(lecture_1, 'C++', 5)
student_1.rate_hw(lecture_2, 'Java', 4)

student_1.rate_hw(reviewer_1, 'Python', 3)
 
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)

reviewer_2.rate_hw(student_2, 'Httml', 9)
 
print(student_1.__dict__)
print(student_2.__dict__)
print(lecture_1.__dict__)
print(lecture_2.__dict__)
print(lecture_3.__dict__)
print(reviewer_1.__dict__)
print(reviewer_2.__dict__)

print(student_1)
print(student_2)

print(reviewer_1)
print(reviewer_2)

print(lecture_1)
print(lecture_2)

student_1 < student_2
student_1 > student_2
student_1 == student_2

student_1 < lecture_2

lecture_1 < lecture_2
lecture_1 > lecture_2
lecture_1 == lecture_2

lecture_1 < student_1

print(assessment_of_homework(list_student, 'Python'))
print(assessment_of_homework(list_student, 'Java'))
print(assessment_for_lectures(list_lecture, 'Python'))
print(assessment_for_lectures(list_lecture, 'Java'))
print(assessment_for_lectures(list_lecture, 'Httml'))