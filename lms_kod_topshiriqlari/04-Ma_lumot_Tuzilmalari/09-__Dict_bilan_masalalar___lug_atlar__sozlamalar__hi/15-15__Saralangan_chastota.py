import sys

input_data = sys.stdin.read().strip()

if input_data:
    chastoto = {}
    
    for harf in input_data:
        chastoto[harf] = chastoto.get(harf, 0) + 1
    saralangan_kalitlar = sorted(chastoto.keys())
    for kalit in saralangan_kalitlar:
        print(f"{kalit}={chastoto[kalit]}")