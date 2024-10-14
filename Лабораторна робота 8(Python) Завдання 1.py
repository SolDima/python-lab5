# Глобальний словник для збереження даних про студентів за групами
students_group = {}

# Функція для додавання студента з унікальним ID
def add_student_with_id(group_number, student_id, full_name, course, subjects_grades):
    # Якщо група ще не існує, створюємо її
    if group_number not in students_group:
        students_group[group_number] = {}
    
    # Створення запису про студента з унікальним ID
    student_info = {
        'ПІБ': full_name,
        'Курс': course,
        'Предмети та оцінки': subjects_grades
    }
    
    # Додаємо студента за унікальним ідентифікатором (ID)
    students_group[group_number][student_id] = student_info
    print(f"Студента {full_name} додано до групи {group_number} з ID {student_id}")

# Функція для редагування оцінок студента
def edit_grades(group_number, student_id, new_grades):
    if group_number in students_group and student_id in students_group[group_number]:
        students_group[group_number][student_id]['Предмети та оцінки'] = new_grades
        print(f"Оцінки студента {students_group[group_number][student_id]['ПІБ']} оновлено")
    else:
        print(f"Студента з ID {student_id} у групі {group_number} не знайдено")

# Функція для виведення інформації про студентів
def display_students():
    for group, students in students_group.items():
        print(f"Група: {group}")
        for student_id, student in students.items():
            print(f"  ID: {student_id}, ПІБ: {student['ПІБ']}, Курс: {student['Курс']}")
            for subject, grade in student['Предмети та оцінки'].items():
                print(f"    {subject}: {grade}")

# Додавання студентів з використанням унікального ID
add_student_with_id('401', 1, 'Іванов Юрій Сергійович', 2, {'Математика': 85, 'Фізика': 90, 'Програмування': 95})
add_student_with_id('401', 2, 'Порощенко Петро Петрович', 2, {'Математика': 75, 'Фізика': 80, 'Програмування': 88})
add_student_with_id('401', 3, 'Яценко Іван Олександрович', 2, {'Математика': 78, 'Фізика': 83, 'Програмування': 85})

# Оновлення оцінок для студента з ID 1
edit_grades('401', 1, {'Математика': 90, 'Фізика': 92, 'Програмування': 97})

# Виведення інформації про студентів
display_students()

#Тепер кожен студент має унікальний ідентифікатор (student_id), що дозволяє однозначно ідентифікувати його в групі.
#Додана функція edit_grades, яка дозволяє оновлювати оцінки студента за його ID.
#Функція display_students тепер виводить інформацію про студентів з урахуванням їх унікальних ID.
