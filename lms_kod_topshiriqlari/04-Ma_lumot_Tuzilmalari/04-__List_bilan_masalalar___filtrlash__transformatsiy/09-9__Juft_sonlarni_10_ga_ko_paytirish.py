n = int(input())
lst = list(map(int, input().split()))
res = []
for x in lst:
    if x % 2 == 0:
        res.append(x * 10)
print(res)