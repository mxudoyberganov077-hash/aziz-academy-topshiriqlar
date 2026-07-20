email = input()
parol = input()

is_valid = ('@' in email) and ('.' in email) and (8 <= len(parol) <= 16) and (email == email.lower())
print(is_valid)