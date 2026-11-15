students = {
    "Aman": 85,
    "Riya": 92,
    "Rahul": 35,
    "Priya": 78,
    "Karan": 30
}

topper = max(students, key=students.get)

average = sum(students.values()) / len(students)

failures = 0

for marks in students.values():
    if marks < 40:
        failures += 1

print("Topper:", topper)
print("Highest Marks:", students[topper])
print("Average Marks:", average)
print("Total Failures:", failures)