a, b = map(int, input().split())
op = input()
if op == "add":
    print(a + b)
elif op == "sub":
    print(a - b)
elif op == "mul":
    print(a * b)
elif op == "div":
    print("Error" if b == 0 else a / b)
   