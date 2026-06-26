a = set(map(int, input().split()))
b = set(map(int, input().split()))
res = sorted(a | b)
print(*res)

