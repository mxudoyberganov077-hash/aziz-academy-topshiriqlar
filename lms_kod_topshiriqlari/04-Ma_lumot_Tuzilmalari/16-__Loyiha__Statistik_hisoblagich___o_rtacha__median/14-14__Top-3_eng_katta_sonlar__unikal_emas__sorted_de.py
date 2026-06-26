nums = list(map(int, input().split()))
unique_nums = list(set(nums))
unique_nums.sort(reverse=True)
top3 = unique_nums[:3]
print(" ".join(map(str, top3)))