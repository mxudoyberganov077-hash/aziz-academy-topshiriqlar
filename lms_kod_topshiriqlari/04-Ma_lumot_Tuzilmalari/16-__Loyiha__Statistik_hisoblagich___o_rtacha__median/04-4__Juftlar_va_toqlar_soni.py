nums = list(map(int, input().split()))
evens_count = 0
odds_count = 0
for x in nums:
    if x % 2 == 0:
        evens_count += 1
    else:
        odds_count += 1
print(evens_count)
print(odds_count)