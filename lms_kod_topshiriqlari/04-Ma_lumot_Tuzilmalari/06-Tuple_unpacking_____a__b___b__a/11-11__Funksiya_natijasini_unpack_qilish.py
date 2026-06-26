def calc(a, b):
    return (a + b, a * b)
a, b = map(int, input().split())
x, y = calc(a, b)
print(x)
print(y)