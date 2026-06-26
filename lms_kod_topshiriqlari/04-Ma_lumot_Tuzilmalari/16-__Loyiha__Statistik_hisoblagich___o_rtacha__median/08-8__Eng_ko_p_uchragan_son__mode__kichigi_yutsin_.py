nums = list(map(int, input().split()))
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1
mode = min(freq.keys(), key=lambda x: (-freq[x], x))
print(mode)