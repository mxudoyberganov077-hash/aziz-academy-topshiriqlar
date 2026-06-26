
A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = set(map(int, input().split()))
faqat_A = A - (B | C)
faqat_B = B - (A | C)
faqat_C = C - (A | B)
natija = faqat_A | faqat_B | faqat_C
if natija:
    print(*(sorted(natija)))
else:
    print("BO'SH")
