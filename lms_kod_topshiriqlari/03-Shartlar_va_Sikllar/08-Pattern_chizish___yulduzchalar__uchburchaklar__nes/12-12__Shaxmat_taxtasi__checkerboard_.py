n, m = map(int, input().split())
for i in range(n):
    print(''.join('*' if (i + j) % 2 == 0 else '.' for j in range(m)))