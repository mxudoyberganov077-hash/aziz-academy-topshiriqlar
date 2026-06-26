words = input().split()
pairs = {(w.lower(), len(w.lower())) for w in words}
sorted_pairs = sorted(pairs, key=lambda x: (x[0], x[1]))
print(len(sorted_pairs))
for word, lenght in sorted_pairs:
    print(f"{word}:{lenght}")