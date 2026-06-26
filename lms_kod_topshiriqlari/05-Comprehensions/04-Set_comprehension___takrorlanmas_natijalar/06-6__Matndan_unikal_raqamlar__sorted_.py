s = input()
digits = set()
for ch in s:
    if ch.isdigit():
        digits.add(ch)
if digits:
    print(" ".join(sorted(digits)))
else:
    print("BO'SH")