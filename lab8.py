
# Словник для збереження даних про студентів
students_group = {}

# Функція для додавання студента до словника
def add_student(group_number, full_name, course, subjects_grades):
    if group_number not in students_group:
        students_group[group_number] = []
    
    student_info = {
        'ПІБ': full_name,
        'Курс': course,
        'Предмети та оцінки': subjects_grades
    }
    
    students_group[group_number].append(student_info)
    print(f"Студента {full_name} додано до групи {group_number}")

# Приклад даних про студента
group_number = '401'
full_name = 'Іванов Юрій Сергійович'
course = 2
subjects_grades = {
    'Математика': 85,
    'Фізика': 90,
    'Програмування': 95
}

# Додавання студента
add_student(group_number, full_name, course, subjects_grades)

# Додавання ще одного студента
add_student('401', 'Порощенко Петро Петрович', 2, {'Математика': 75, 'Фізика': 80, 'Програмування': 88})

# Виведення результату
for group, students in students_group.items():
    print(f"Група: {group}")
    for student in students:
        print(f"  ПІБ: {student['ПІБ']}, Курс: {student['Курс']}")
        for subject, grade in student['Предмети та оцінки'].items():
            print(f"    {subject}: {grade}")
