
n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
eng_yaxshi = max(students, key=lambda x: x['score'])
print(eng_yaxshi ['name'])
