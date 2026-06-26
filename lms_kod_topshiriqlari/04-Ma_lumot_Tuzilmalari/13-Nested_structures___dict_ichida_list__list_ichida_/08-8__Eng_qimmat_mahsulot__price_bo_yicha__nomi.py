
n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})
eng_qimmat = items[0]
for item in items:
    if item['price'] > eng_qimmat['price']:
        eng_qimmat = item
print(eng_qimmat['name'])
