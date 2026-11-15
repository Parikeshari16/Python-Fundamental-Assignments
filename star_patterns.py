n = int(input("Enter number of rows: "))

# 1. Right Triangle
print("Right Triangle")
for i in range(1, n + 1):
    print("* " * i)

# 2. Pyramid
print("Pyramid")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# 3. Diamond
print("Diamond")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)