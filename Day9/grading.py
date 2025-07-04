from distutils.command.sdist import sdist

students_scores = {
    "Harry": 88,
    "Mary": 78,
    "June": 95,
    "Kelly": 75,
    "Draco": 60
}

students_grades = {}

for students in students_scores:
    if students_scores[students] > 91:
        students_grades[students] = "Outstanding"
    elif students_scores[students] >= 80:
        students_grades[students] = "Exceeds Expectations"
    elif students_scores[students] >= 70:
        students_grades[students] = "Acceptable"
    else:
        students_grades[students] = "Fail"

print(students_grades)