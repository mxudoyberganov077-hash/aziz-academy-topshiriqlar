elements = input().split()
seen = []

for item in elements:
    if item not in seen:
        seen.append(item)
print(*seen)