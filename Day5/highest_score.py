students_scores = [150, 120, 139, 152, 110, 116, 55, 59, 180, 172]
#
# total_exam_score = sum(students_scores)
# print(f"Total score {total_exam_score}" )

max_score = 0

for score in students_scores:
    if score > max_score:
        max_score = score

print(max_score)