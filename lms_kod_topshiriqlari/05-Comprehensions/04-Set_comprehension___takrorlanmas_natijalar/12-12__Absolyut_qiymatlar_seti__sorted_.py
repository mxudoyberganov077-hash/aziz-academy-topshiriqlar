nums = list(map(int, input().split()))
s = {abs(x) for x in nums}
print(" ".join(map(str, sorted(s))))