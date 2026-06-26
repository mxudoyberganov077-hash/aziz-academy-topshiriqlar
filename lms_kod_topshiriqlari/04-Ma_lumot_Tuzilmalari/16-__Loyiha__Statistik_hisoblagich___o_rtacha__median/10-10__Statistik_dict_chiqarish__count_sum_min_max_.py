nums = list(map(int, input().split()))
stats = {
    'count': len(nums),
    'sum': sum(nums),
    'min': min(nums),
    'max': max(nums)
}
print(stats)