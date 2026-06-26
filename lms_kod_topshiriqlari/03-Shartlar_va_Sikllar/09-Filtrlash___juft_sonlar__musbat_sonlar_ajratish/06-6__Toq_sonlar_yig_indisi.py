n = int(input())
nums = list(map(int, input().split()))
summa = 0
for x in nums:
    if x % 2 != 0:
        summa += x
print(summa)