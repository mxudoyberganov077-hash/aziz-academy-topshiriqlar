nums = list(map(int, input().split()))
mean = sum(nums) / len(nums)
rng = max(nums) - min(nums)
if rng == 0:
    result = [0.00 for _ in nums]
else:
    result = [(x - mean) / rng for x in nums]
print(" ".join(f"{z:.2f}" for z in result))