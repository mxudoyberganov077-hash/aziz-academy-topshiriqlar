s = input()
words = s.split()
lengths = set()
for w in words:
    lengths.add(len(w))
if lengths:
    print(" ".join(map(str, sorted(lengths))))
else:
    print("BO'SH")