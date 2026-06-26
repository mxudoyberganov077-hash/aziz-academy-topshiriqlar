# INPUT:
# n (mahsulotlar soni)
# n qator: name price qty
# Har mahsulot dict: {'name':..., 'price':..., 'qty':...}
# Vazifa: umumiy summa = Σ(price*qty)

n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})
umumiy_summa = 0
for item in items:
    umumiy_summa += item['price'] * item['qty']
print(umumiy_summa)
