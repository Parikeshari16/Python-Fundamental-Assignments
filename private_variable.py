class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def display_salary(self):
        print("Salary:", self.__salary)

obj = Employee(30000)
obj.display_salary()