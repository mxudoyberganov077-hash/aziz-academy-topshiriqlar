n = int(input())
yigindi = 0
sikl = 0
while sikl < n:
    son = int(input())
    sikl += 1
    
    if son <= 0:
        continue
        
    yigindi += son
    
print(yigindi)