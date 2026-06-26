n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = int(value)
    
x = int(input())
res = {}
for key, value in d.items():
    if value >= x:
        res[key] = value
print(res)