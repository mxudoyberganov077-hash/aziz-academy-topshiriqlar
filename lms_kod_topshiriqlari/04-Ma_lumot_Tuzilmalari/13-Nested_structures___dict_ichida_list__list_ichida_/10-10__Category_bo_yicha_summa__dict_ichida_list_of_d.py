

n = int(input().strip())
items = []
for _ in range(n):
    cat, name, price, qty = input().split()
    items.append({'cat': cat, 'name': name, 'price': int(price), 'qty': int(qty)})
totals = {}
for item in items:
    totals[item['cat']] = totals.get(item['cat'], 0) + item['price'] * item['qty']
for cat in sorted(totals):
    print(cat, totals[cat])