n = int(input())
print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7}")
print("------------+-----+-------")
for _ in range(n):
    product, qty, price = input().split()
    qty = int(qty)
    price = int(price)
    print(f"{product:<12} | {qty:>5} | {price:>7}")