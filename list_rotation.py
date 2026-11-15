lst = [1, 2, 3, 4, 5]

k = int(input("Enter rotation value: "))
direction = input("Enter L for left or R for right: ")

k = k % len(lst)

if direction == "L":
    result = lst[k:] + lst[:k]
else:
    result = lst[-k:] + lst[:-k]

print("Rotated list:", result)