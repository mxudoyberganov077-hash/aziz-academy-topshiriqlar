
n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
eng_katta = students[0]['score']
for student in students:
    if student['score'] > eng_katta:
        eng_katta = student['score']
print(eng_katta)
