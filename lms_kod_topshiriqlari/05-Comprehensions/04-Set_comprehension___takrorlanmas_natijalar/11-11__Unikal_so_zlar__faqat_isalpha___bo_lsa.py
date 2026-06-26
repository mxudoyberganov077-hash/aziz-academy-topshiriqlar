tokens = input().split()
words = {t.lower() for t in tokens if t.isalpha()}
if words:
    print(" ".join(sorted(words)))
else:
    print("BO'SH")