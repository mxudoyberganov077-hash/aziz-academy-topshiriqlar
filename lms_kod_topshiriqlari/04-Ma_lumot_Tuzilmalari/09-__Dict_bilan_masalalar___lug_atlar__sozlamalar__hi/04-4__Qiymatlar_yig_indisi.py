n = int(input())

lugat = {}

for i in range(n):
    son = int(input())
    lugat[f"k{i}"] = son
yigindi = sum(lugat.values())
print(yigindi)