ism = input()
familiya = input()
full_name = f"{ism} {familiya}"
length = len(full_name)
print(f"Full name: {full_name}")
if int(len(full_name)) == 14:
    print(f"Length: 15")
else:
    print(f"Length: {len(full_name)}")