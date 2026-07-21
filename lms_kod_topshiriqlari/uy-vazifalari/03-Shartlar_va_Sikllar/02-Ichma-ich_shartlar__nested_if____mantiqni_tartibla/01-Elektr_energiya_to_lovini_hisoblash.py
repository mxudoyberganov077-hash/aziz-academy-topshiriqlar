kwh = int(input())

if kwh < 0:
    print("Notogri qiymat")
elif kwh <= 100:
    tolov = kwh * 450
    print(tolov)
elif kwh <= 200:
    tolov = 100 * 450 + (kwh - 100) * 600
    print(tolov)
else:
    tolov = 100 * 450 + 100 * 600 + (kwh - 200) * 900
    print(tolov)