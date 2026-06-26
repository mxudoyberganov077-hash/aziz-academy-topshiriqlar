n = int(input())
lst = list(map(int, input().split()))
res = []
for x in lst[:n]:
    if x > 0:
        res.append(x * 2)
print(res)