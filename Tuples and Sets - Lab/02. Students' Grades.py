def found_average_grade(grades):
    return sum(grades) / len(grades)


num_of_students = int(input())

students_marks = {}

for _ in range(num_of_students):

    name, grade = input().split()

    if name not in students_marks:
        students_marks[name] = []
    students_marks[name].append(float(grade))

for student, grades in students_marks.items():
    grades_str = ' '.join(str(f'{x:.2f}') for x in grades)
    print(f"{student} -> {grades_str} (avg: {found_average_grade(grades):.2f})")
