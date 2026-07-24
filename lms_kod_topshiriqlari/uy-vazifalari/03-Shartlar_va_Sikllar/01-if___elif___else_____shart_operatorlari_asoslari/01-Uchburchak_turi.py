import sys

input_data = sys.stdin.read().split()

if len(input_data) >= 3:
    a = int(input_data[0])
    b = int(input_data[1])
    c = int(input_data[2])
    
    if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
        if a == b == c:
            print("teng tomonli")
        elif a == b or a == c or b == c:
            print("teng yonli")
        else:
            print("turli tomonli")
else:
            print("notogri")