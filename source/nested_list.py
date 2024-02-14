n = int(input())

students = []

for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

students.sort(key=lambda x: x[1])

second_highest_score = -1

for student in students:
    if student[1] > students[0][1]: second_highest_score = student[1]


for student in sorted([s[0] for s in students if s[1] == second_highest_score]): print(student)