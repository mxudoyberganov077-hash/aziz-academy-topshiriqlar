words = input().split()
s = {words.lower() for words in words}
print(*sorted(s))
 