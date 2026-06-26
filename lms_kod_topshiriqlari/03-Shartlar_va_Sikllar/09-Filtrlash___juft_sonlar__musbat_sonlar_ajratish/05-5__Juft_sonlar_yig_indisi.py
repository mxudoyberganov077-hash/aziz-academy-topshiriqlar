n = int(input())
summa = 0
nums = list(map(int, input().split()))
for x in nums:
    if x % 2 == 0:
        summa += x
print(summa)
