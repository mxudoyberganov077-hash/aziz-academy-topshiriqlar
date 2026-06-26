
a = set(map(int, input().split()))
b = set(map(int, input().split()))
res = a & b
if len(res) == 0:
    print("BO'SH")
else:
    print(*sorted(res))

