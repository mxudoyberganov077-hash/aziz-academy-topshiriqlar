n = int(input())
lst = list(map(int, input().split()))
res = []
for x in lst:
    if 0 < x < 100:
        res.append(x)
print(res)