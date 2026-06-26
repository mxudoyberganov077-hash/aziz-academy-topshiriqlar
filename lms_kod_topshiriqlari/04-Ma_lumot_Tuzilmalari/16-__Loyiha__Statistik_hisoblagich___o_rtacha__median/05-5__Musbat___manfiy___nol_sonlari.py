nums = list(map(int, input().split()))
positives_count = 0
negatives_count = 0
zeros_count = 0
for n in nums:
    if n > 0:
        positives_count += 1
    elif n < 0:
        negatives_count += 1
    else:
        zeros_count += 1
print(positives_count)
print(negatives_count)
print(zeros_count)