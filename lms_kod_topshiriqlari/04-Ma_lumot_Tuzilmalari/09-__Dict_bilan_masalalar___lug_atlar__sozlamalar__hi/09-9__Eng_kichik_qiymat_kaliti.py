n = int(input())

eng_kichik_qiymat = float('inf')
eng_yaxshi_kalit = None

for _ in range(n):
    kalit, qiymat = input().split()
    qiymat = int(qiymat)
    if qiymat < eng_kichik_qiymat:
        eng_kichik_qiymat = qiymat
        eng_yaxshi_kalit = kalit
print(eng_yaxshi_kalit)