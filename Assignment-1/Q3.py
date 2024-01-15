# Write a Python program to check the validity of password input by users.
# Validation:
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

Pass = input('Enter the password : ')
leng = len(Pass)
def validation (Pass, length):
    if length < 6 or length > 16:
        return False
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special_char = False
    for ch in Pass:
        i = ord(ch)
        if i in range (48,58):
            has_digit = True;
        elif i in range (65,91):
            has_uppercase = True;
        elif i in range (97,123):
            has_lowercase = True;
        elif ch in ['#', '$', '@']: 
            has_special_char = True;
        else:
            return False
    return has_digit and has_uppercase and has_lowercase and has_special_char
    
result = validation (Pass, leng)
print(result)
