class LengthError(Exception):
    pass

class UppercaseError(Exception):
    pass

class NumberError(Exception):
    pass

try:
    password = input("Enter password: ")

    if len(password) < 8:
        raise LengthError("Password must contain at least 8 characters")

    if not any(ch.isupper() for ch in password):
        raise UppercaseError("Password must contain an uppercase letter")

    if not any(ch.isdigit() for ch in password):
        raise NumberError("Password must contain a number")

    print("Password Valid")

except LengthError as e:
    print("Error:", e)

except UppercaseError as e:
    print("Error:", e)

except NumberError as e:
    print("Error:", e)