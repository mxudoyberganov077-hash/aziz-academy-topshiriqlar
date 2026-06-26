n = int(input())
nums = list(map(int, input().split()))
for x in nums:
    if x > 0 and x % 2 == 0:
        print(x)