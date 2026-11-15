
salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))
age = int(input("Enter your age: "))

if salary >= 30000 and credit_score >= 700 and 21 <= age <= 60:
    print("Loan Approved")

elif (salary >= 30000 and credit_score >= 700) or \
     (salary >= 30000 and 21 <= age <= 60) or \
     (credit_score >= 700 and 21 <= age <= 60):
    print("Conditionally Approved")

else:
    print("Loan Rejected")
