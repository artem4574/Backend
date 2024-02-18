n = int(input())
records = []

for _ in range(n):
    name = input()
    grade = float(input())
    records.append([name, grade])

sorted_records = sorted(records, key=lambda x: x[1], reverse=True)

second_highest_grade = sorted(set(x[1] for x in sorted_records))[-2]

second_highest_students = [record[0] for record in sorted_records if record[1] == second_highest_grade]

second_highest_students.sort()

for student in second_highest_students: print(student)
