import sys
input_data = sys.stdin.read().splitlines()

if input_data:
    n = int(input_data[0])
    ballar_lugati = {}
    
    i = 1
    while i <= n:
        
        ism, ball = input_data[i].split()
        
        ballar_lugati[ism] = int(ball)
        i += 1
print(sum(ballar_lugati.values()))