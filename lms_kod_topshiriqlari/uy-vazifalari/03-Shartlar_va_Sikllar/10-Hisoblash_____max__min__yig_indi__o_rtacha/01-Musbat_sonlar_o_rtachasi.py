n = int(input())

musbat_yigindi = 0
musbat_soni = 0

for i in range(n):
    son = int(input())
    if son > 0:
        musbat_yigindi += son
        musbat_soni += 1
if musbat_soni > 0:
    natija = musbat_yigindi // musbat_soni
    print(natija)
else:
    print(0)