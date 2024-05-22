students = ["José", "Joana", "Maria", "Carla", "Mauricio", "Andre", "Tiago", "Enzo", "Amanda", "Alessandra"]
grades = [
    [10, 9, 8, 8],
    [9, 7, 6, 4],
    [10, 10, 10, 10],
    [5, 3, 10, 9],
    [7, 6, 6, 6],
    [7, 7, 8, 7],
    [7, 7, 7, 9],
    [8, 5, 6, 7],
    [10, 9, 7, 4],
    [10, 1, 3, 3],
]
avg_grades = []
for notes in grades:
    sum_grade = 0
    for note in notes:
        sum_grade += note
    avg_grades.append(sum_grade / len(notes))

smarter_students = 0
for note in avg_grades:
    if note > 7:
        smarter_students += 1

for i, student in enumerate(students):
    print(student, "averange grade: ", avg_grades[i])
print("Students with grades higher than 7:", smarter_students)
