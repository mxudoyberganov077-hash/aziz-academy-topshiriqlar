n = int(input())
lst = input().split()
res = []
for x in lst[:n]:
    if len(x) >= n:
        res.append(x)
print(res)