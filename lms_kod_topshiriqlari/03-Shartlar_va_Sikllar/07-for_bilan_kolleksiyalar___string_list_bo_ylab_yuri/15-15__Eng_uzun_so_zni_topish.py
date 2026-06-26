s = input()
words = s.split()
eng_uzun_soz = ""
for word in words:
    if len(word) > len(eng_uzun_soz):
        eng_uzun_soz = word
print(eng_uzun_soz)