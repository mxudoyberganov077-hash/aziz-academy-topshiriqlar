n = int(input())

first = int(input())
max_val = first
min_val = first

for _ in range(n - 1):
    num = int(input())
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print(max_val - min_val)