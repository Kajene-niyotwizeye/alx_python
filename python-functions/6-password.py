def validate_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if the password contains at least one uppercase letter, one lowercase letter, and one digit
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

        # If all required types of characters are found, break the loop early
        if has_uppercase and has_lowercase and has_digit:
            break

    if not (has_uppercase and has_lowercase and has_digit):
        return False

    # Check if the password contains any spaces
    if ' ' in password:
        return False

    # If all checks pass, return True
    return True

# Test cases
print(validate_password("Abc123"))  # True
print(validate_password("Password123"))  # True
print(validate_password("hello world"))  # False (contains a space)
print(validate_password("Short1"))  # False (less than 8 characters)
print(validate_password("NOLOWERNUM"))  # False (no lowercase letter)

