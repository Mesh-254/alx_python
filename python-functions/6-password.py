#!/usr/bin/python3
def validate_password(password):
    """Password Validation Function"""
    # Check if the password is at least 8 characters long.
    if len(password) < 8:
        return False

    # Check if the password contains at least one uppercase letter.
    if not any(char.isupper() for char in password):
        return False

    # Check if the password contains at least one lowercase letter.
    if not any(char.islower() for char in password):
        return False

    # Check if the password contains at least one digit.
    if not any(char.isdigit() for char in password):
        return False

    # Check if the password contains space.
    if password.find(" ") != -1:
        return False
    # The password meets all of the requirements, so return True.
    return True
