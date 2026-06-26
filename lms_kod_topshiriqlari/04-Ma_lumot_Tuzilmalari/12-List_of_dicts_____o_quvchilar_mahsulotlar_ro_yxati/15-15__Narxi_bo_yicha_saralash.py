
n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
products.sort(key=lambda x: x['price'])
for product in products:
    print(f"{product['name']} {product['price']}")

