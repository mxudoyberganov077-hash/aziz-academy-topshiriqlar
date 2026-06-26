
s1 = input().strip().lower().split()
s2 = input().strip().lower().split()
res = set(s1) | set(s2)
print(len(res))
