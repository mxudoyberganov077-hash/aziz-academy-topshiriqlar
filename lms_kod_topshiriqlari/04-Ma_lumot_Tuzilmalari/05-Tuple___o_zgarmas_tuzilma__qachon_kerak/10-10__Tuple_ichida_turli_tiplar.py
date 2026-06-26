def tekshir(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x
print(tuple(tekshir(x) for x in input().split()))