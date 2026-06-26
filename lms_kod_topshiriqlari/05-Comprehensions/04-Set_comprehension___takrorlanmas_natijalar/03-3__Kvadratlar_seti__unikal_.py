nums = list(map(int, input().split()))
s = {x * x for x in nums}
print(*sorted(s))