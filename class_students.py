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
            return 'Ошибка' 

    def __str__(self):

        '''Выводит на печать имя и фамилию объекта класса'''

        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'man')
best_student.courses_in_progress += ['Python', 'Java']
best_student.finished_courses += ['C++']
best_student_2 = Student('Mila', 'Rem', 'woman')
best_student_2.courses_in_progress += ['Python']

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
best_student.rate_hw(cool_lecture_2, 'Java', 4)

print(best_student.rate_hw(cool_reviewer, 'Python', 3))
 
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student_2, 'Python', 10)
cool_reviewer.rate_hw(best_student_2, 'Python', 9)
 
print(best_student.grades)
print(best_student.__dict__)
print(cool_lecture.__dict__)
print(cool_reviewer.__dict__)
print(cool_lecture_2.__dict__)
print(best_student)
print(best_student_2)
print(cool_reviewer)
print(cool_lecture)
print(cool_lecture_2)

