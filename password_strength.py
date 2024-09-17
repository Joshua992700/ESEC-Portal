import re

def check_password_strength(password):
    if len(password) < 8:
        return "Your Password is Not Strong"
    
    if not re.search("[a-z]", password):
        return "Your Password is Not Strong"
    
    if not re.search("[A-Z]", password):
        return "Your Password is Not Strong"
    
    if not re.search("[0-9]", password):
        return "Your Password is Not Strong"
    
    if not re.search("[^A-Za-z0-9]", password):
        return "Your Password is Not Strong"
    
    return "Your Password is Strong"

password = input()
print(check_password_strength(password))
