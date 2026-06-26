s = input()
words = s.split()
letters = set()
for w in words:
    if w:
        letters.add(w[0].lower())
if letters:
    print(" ".join(sorted(letters)))
else:
    print("BO'SH")