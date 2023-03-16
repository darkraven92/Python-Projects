import re

def check_password_strength(password):
    # Define a pattern for a strong password, containing at least 8 characters, one uppercase letter,
    # one lowercase letter, one digit, and one special character
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    # Check if the password matches the pattern
    if re.match(pattern, password):
        return "strong"
    
    # If not, check if it meets the criteria for a medium password, containing at least 6 characters and
    # either an uppercase letter, a lowercase letter, a digit, or a special character
    elif re.match(r"^(?=.*[a-zA-Z])(?=.*\d|[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$", password):
        return "medium"
    
    # If not, the password is considered weak
    else:
        return "weak"
    
# Prompt the user to enter a password and check its strength
password = input("Enter a password: ")
strength = check_password_strength(password)
print(f"The password '{password}' is {strength}.")
