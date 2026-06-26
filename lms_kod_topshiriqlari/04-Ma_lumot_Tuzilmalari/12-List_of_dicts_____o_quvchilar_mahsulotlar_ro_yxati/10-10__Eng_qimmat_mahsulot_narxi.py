
n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
max_price = 0
for product in products:
    if product['price'] > max_price:
        max_price = product['price']
print(max_price)

