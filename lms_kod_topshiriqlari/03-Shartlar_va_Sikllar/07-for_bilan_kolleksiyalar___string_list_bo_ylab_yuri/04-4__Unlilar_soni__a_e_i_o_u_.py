s = input()
unlilar = "aeiou"
count = 0
for ch in s:
    if ch in unlilar:
        count += 1
print(count)