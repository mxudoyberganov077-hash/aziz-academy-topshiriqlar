words = input().split()
fraq = {}
for w in words:
    fraq[w] = fraq.get(w, 0) + 1
    
for word in sorted(fraq.keys()):
    print(f"{word} {fraq[word]}")