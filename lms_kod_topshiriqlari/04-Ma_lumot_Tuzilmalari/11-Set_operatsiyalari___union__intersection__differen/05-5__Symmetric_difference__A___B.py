
a = set(map(int, input().split()))
b = set(map(int, input().split()))
res = sorted(a ^ b)
if not res:
    print("BO'SH")
else:
    print(*res)
