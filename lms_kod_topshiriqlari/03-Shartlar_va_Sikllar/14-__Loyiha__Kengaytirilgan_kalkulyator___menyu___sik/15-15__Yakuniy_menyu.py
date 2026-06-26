a, b = map(int, input().split())
while True:
    tanlov = int(input())
    if tanlov == 1:
        print(a + b)
    elif tanlov == 2:
        print(a - b)
    elif tanlov == 3:
        print(a * b)
    elif tanlov == 4:
        print(a / b)
    elif tanlov == 0:
        print("Exit")
        break