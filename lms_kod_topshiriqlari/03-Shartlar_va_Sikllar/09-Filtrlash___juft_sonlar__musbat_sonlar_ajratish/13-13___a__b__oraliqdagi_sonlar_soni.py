n = int(input())
nums = list(map(int, input().split()))
a, b = map(int, input().split())
count = 0
for x in nums:
    if a <= x <= b:
        count += 1
print(count)