# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# # print(range(1, 10))
# sum = 0
# for score in student_scores:
#     sum += score
# print(sum)

student_scores1 = [8, 65, 89, 86, 55, 91, 64, 89]
# highest_score = max(student_scores1)
# print(highest_score)
max_score = 0
for score in student_scores1:
    if score > max_score:
        max_score = score
print(max_score)

