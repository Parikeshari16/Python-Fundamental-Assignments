def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

x = int(input("Enter base: "))
n = int(input("Enter exponent: "))

print("Power:", power(x, n))