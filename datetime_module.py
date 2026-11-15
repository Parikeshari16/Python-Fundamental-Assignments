import datetime

now = datetime.datetime.now()

print("Current Date:", now.date())
print("Current Time:", now.time())

birth_year = int(input("Enter your birth year: "))

age = now.year - birth_year

print("Your age is:", age)