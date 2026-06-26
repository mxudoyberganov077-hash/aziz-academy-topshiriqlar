
A = set(input().strip().split())
B = set(input().strip().split())
ikkalasida_bor = A & B
print(len(ikkalasida_bor))
for ism in sorted(ikkalasida_bor):
    print(ism)