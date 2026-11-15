library = {
    "Python": 5,
    "Java": 3,
    "C++": 4,
    "DSA": 2
}

print("Available Books:", library)

book = input("Enter book name: ")

if book in library and library[book] > 0:
    library[book] -= 1
    print("Book issued successfully")
else:
    print("Book not available")

print("Updated Library:", library)