s = input()
count = 0
for ch in s:
    if '0' <= ch <= '9':
        count += 1
print(count)