N = int(input())
teskari_son = 0
if N == 0:
    teskari_son = 0
else:
     while N > 0:
        oxirgi_raqam = N % 10
        teskari_son = (teskari_son * 10) + oxirgi_raqam
        N //= 10
print(teskari_son)