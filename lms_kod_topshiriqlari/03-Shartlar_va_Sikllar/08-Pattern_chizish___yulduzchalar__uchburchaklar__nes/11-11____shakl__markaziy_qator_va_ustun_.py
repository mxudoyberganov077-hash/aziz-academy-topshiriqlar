n = int(input())
center = n // 2
for i in range(n):
    if i == center:
        print('*' * n)
    else:
        print('.' * center + '*' + '.' * center)