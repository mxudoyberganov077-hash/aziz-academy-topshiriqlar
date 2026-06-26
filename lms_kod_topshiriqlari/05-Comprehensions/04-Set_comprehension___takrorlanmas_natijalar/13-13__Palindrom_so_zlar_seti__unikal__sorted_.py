words = input().split()
palindromes = {w.lower() for w in words if w.lower() == w.lower()[::-1]}
if palindromes:
    print(" ".join(sorted(palindromes)))
else:
    print("BO'SH")