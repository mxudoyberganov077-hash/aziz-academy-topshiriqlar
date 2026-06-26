s = input().lower()
vowels = set()
for ch in s:
    if ch in "aeiou":
        vowels.add(ch)
if vowels:
    print(" ".join(sorted(vowels)))
else:
    print("BO'SH")