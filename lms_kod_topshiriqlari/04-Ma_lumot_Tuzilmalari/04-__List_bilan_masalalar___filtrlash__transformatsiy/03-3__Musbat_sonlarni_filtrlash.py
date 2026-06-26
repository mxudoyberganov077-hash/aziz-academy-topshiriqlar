n = int(input())
lst = list(map(int, input().split()))
res = []
for x in lst:
    if x > 0:
        res.append(x)
print(res)