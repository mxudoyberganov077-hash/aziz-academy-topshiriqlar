n = int(input())
lst = list(map(int, input().split()))
res = []
for x in lst:
    res.append(abs(x))
print(res)