s = input()

hisob = {}
tartib = []

for h in s:
    if h not in hisob:
        hisob[h] = 0
        tartib.append(h)
    hisob[h] += 1
        
natija = [f"{h}:{hisob[h]}" for h in tartib]
print(*(natija))