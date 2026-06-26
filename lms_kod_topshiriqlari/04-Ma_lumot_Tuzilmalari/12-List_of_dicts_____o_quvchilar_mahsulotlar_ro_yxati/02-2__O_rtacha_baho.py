
n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
jami_baho = 0
for student in students:
    jami_baho += student['score']
ortacha_baho = jami_baho / n
print(ortacha_baho)
