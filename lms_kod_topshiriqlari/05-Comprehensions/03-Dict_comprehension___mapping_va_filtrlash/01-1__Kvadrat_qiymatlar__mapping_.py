n = int(input())
data = {}
for _ in range(n):
    k, v = input().split()
    data[k] = int(v) ** 2
print({k: v for k, v in data.items()})