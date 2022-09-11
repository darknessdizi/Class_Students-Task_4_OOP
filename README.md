# Решение задачи №4

1. Добавлены дочерние классы Lecture и Reviewer. Родитель класс Mentor.
2. Оценки студентам могут ставить только Reviewer.
3. Студенты могут ставить оценки для Lecture. (Решена задача №2)
4. Перегружен магический метод __str__ у Lecture и Reviewer
5. Добавлен метод __average_rating у Lecture
6. Перегружен магический метод __str__ у Student
7. Добавлен метод __average_rating у Student
8. Добавлены методы сравнения __lt__ и __eq__ для Student
9. Добавлены методы сравнения __lt__ и __eq__ для Lecture (Решена задача №3)
10. Создаем объекты классов
11. Добавлены функции assessment_of_homework и assessment_for_lectures