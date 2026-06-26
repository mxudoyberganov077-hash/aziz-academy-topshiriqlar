n = int(input())
ans = 0
for i in range(n - 1, 0, -1):
    if n % i == 0:
        ans = i
        break
print(ans)