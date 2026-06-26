n = int(input())
a = list(map(int, input().split()))
b = [x for x in a if x % 2]
print(max(b) if b else "No")