n = int(input())
numbers = list(map(int, input().split()))
mnimum = numbers[0]
for x in numbers:
    if x < mnimum:
        mnimum = x
print(mnimum)