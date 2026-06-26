n = int(input())
lst = input().split()
res = []
for x in lst[:n]:
    res.append(len(x))
print(res)