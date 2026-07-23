k = int(input())
config = {}
for _ in range(k):
    kalit, qiymati = input().split()
    config[kalit] = int(qiymati)
q = int(input())
for _ in range(q):
    kalit = input().strip()
    print(config.get(kalit, 0))
    