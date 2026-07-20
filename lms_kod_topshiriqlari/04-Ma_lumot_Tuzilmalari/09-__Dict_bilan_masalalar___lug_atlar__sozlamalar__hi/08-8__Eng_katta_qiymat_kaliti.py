n = int(input())

max_key = None
max_value = float('-inf')

for _ in range(n):
    key, val_str = input().split()
    val = int(val_str)
    
    if val > max_value:
        max_value = val
        max_key = key
        
print(max_key)