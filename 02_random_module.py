import random
import string

# Generate OTP
otp = random.randint(100000, 999999)
print("OTP:", otp)

# Generate random password
characters = string.ascii_letters + string.digits
password = ''.join(random.choices(characters, k=8))
print("Password:", password)

# Generate random list
numbers = [random.randint(1, 100) for i in range(5)]
print("Random numbers:", numbers)