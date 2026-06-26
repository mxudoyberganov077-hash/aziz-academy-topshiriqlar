
n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
count = 0
for student in students:
    if student['score'] > 80:
        count += 1
print(count) 

