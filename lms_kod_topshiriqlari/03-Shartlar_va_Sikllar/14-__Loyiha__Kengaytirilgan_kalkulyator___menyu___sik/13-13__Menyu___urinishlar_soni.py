s = ""
while "0" not in s:
    s += " " + input()
print(s.split().index("0") // 3)