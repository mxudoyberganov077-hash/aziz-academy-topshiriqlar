nums = list(map(int, input().split()))
mean = sum(nums) / len(nums)
result = [(x - mean) for x in nums]
print(" ".join(f"{x:.2f}" for x in result))