n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
new_d = {}
for k, v in d.items():
    new_d[k] = v * 2
print(new_d)