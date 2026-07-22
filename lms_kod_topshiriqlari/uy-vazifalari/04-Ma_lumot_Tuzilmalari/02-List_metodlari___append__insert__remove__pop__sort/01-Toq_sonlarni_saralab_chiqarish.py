n = int(input())
toq_sonlar = []

for _ in range(n):
    num = int(input())
    if num % 2 != 0:
        toq_sonlar.append(num)
        
toq_sonlar.sort()

print(*toq_sonlar)