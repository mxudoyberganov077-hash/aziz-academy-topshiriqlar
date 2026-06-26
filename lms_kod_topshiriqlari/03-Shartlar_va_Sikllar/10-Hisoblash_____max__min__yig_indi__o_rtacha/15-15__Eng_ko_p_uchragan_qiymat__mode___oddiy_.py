n = int(input())
a = list(map(int, input().split()))
print(min(a, key=lambda x: (-a.count(x), x)))