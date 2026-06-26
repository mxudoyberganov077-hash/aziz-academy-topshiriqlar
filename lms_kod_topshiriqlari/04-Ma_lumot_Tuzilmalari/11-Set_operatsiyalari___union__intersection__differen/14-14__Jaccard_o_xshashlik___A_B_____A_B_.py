
A = set(map(int, input().split()))
B = set(map(int, input().split()))
kesishma_uzunligi = len(A & B)
birlashma_uzunligi = len(A | B)
jaccard = kesishma_uzunligi / birlashma_uzunligi
print(f"{jaccard:.3f}")
