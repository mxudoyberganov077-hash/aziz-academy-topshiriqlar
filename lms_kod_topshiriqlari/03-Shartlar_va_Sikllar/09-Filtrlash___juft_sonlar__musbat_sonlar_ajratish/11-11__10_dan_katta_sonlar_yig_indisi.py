n = int(input())
nums = list(map(int, input().split()))
print(sum(x for x in nums if x > 10))