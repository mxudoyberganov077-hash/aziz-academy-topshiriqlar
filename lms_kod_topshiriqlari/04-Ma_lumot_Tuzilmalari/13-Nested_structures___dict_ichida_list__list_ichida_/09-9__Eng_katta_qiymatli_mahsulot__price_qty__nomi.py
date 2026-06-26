
n = int(input().strip())
items = []
for _ in range(n):
    name, price, qty = input().split()
    items.append({'name': name, 'price': int(price), 'qty': int(qty)})
max_value = -1
best_product = ""
for item in items:
    current_value = item['price'] * item['qty']
    if current_value > max_value:
        max_value = current_value
        best_product = item['name']
print(best_product)
