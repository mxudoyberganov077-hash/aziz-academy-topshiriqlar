n = int(input())
lst = list(map(int, input().split()))
first, *rest = lst
print(first)
print(rest)