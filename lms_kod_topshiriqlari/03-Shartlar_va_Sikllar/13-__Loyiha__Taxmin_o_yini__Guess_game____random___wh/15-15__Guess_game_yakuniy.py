yashirin_son = 20
urinishlar = 0

while True:
    son = int(input())
    urinishlar += 1
    if son == 25:
        print("Invalid")
        
    elif son < yashirin_son:
            print("Low")
    else:
            print("Correct")
            break
print(urinishlar)
           