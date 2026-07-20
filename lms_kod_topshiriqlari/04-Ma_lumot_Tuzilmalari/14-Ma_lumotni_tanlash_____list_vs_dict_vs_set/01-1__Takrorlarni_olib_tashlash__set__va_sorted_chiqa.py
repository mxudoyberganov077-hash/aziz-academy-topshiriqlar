sonlar = list(map(int, input().split()))

unikal_saralangan = sorted(set(sonlar))
print(*(unikal_saralangan))