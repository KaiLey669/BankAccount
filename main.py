class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        self.__deposit = 0

    def add_money_to_balance(self, amount):
        if amount <= 0:
            print("Пополнение должно быть больше 0.")
            return
        self.__balance += amount
        print(f"Баланс пополнен. Текущий баланс: {self.__balance}")

    def print_balance(self):
        print(f"Текущий баланс: {self.__balance}")

    def withdraw_money(self, amount):
        if amount <= 0:
            print(f"Введено некорретное значение.")
            return

        new_balance = self.__balance - amount
        if new_balance >= 0:
            self.__balance = new_balance
            print(f"Деньги успешно сняты. Текущий баланс: {self.__balance}")
        else:
            print("Недостаточно средств.")

    def add_money_to_deposit(self, amount):
        if amount <= 0:
            print(f"Введено некорретное значение.")
            return

        if amount <= self.__balance:
            self.__balance -= amount
            self.__deposit += amount
            print(f"Деньги поступили на депозит: {self.__deposit}")
        else:
            print("Недостаточно средств.")


bank_account = BankAccount(100)
bank_account.print_balance()
bank_account.withdraw_money(50)
bank_account.add_money_to_deposit(30)
bank_account.print_balance()
bank_account.withdraw_money(100)
bank_account.add_money_to_deposit(100)
bank_account.add_money_to_balance(50)
