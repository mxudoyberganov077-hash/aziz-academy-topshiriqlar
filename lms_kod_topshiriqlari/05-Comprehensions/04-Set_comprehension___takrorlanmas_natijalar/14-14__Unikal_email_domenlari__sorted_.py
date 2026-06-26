emails = input().split()
domains = {e.split("@")[1].lower() for e in emails if "@" in e}
if domains:
    print(" ".join(sorted(domains)))
else:
    print("BO'SH")