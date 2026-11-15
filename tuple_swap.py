t = (10, 20, 30, 40, 50)

a, *middle, b = t

t = (b, *middle, a)

print("Updated tuple:", t)