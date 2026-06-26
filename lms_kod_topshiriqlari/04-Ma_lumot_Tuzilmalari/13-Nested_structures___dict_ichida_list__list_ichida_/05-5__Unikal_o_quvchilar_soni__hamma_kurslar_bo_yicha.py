
n = int(input().strip())
courses = []
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    courses.append({'name': name, 'students': students})
    all_students = set()
    for c in courses:
        all_students.update(c['students'])
print(len(all_students))
