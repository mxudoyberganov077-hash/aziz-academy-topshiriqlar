nums = list(map(int, input().split()))
s = {x for x in nums}
print(*sorted(s))