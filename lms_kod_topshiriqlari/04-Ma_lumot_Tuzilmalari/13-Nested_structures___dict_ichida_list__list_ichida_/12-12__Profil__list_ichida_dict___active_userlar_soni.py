
n = int(input().strip())
cnt = 0
for _ in range(n):
    username, active = input().split()
    if active == '1':
        cnt += 1
print(cnt)

