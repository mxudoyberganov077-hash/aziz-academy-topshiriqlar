n = int(input())
print("Name       | Grade")
print("----------+------")
for _ in range(n):
    name, score = input().split()
    score = int(score)
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"{name:<10} |   {grade}")