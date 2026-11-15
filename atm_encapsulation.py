class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def check_balance(self, pin):
        if pin == self.__pin:
            print("Balance:", self.__balance)
        else:
            print("Incorrect PIN")

    def withdraw(self, pin, amount):
        if pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful")
                print("Remaining Balance:", self.__balance)
            else:
                print("Insufficient balance")
        else:
            print("Incorrect PIN")

obj = ATM(1234, 5000)

obj.check_balance(1234)
obj.withdraw(1234, 1000)