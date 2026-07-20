n = int(input())

hisob = {}
sozlar = []

for _ in range(n):
    soz = input()
    if soz not in hisob:
        hisob[soz] = 0
        sozlar.append(soz)
    hisob[soz] += 1
        
eng_kop = max(sozlar, key=hisob.get)
print(eng_kop)