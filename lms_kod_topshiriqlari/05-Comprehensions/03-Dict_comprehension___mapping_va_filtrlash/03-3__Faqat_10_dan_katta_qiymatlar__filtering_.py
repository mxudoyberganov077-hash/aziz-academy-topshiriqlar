n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    value = int(value)
    if value > 10:
        d[key] = value
print(d)