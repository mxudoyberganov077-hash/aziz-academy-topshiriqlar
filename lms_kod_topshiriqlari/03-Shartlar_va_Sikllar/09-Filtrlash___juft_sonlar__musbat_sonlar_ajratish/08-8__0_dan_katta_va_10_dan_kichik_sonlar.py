n = int(input())
nums = list(map(int, input().split()))
for i in nums:
    if i > 0 and i < 10:
        print(i)