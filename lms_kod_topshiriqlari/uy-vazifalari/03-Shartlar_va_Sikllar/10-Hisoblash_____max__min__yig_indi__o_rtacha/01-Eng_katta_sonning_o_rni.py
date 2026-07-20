n = int(input())

max_son = int(input())
max_pos = 1

for i in range(2, n + 1):
    son = int(input())
    if son > max_son:
        max_son = son
        max_pos = i
print(max_pos)