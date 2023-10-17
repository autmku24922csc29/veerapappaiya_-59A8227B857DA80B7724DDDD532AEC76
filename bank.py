class BankAccount:
  def _init_(self, account_number, account_holder_name, initial_balance):
      self._account_number = account_number
      self._account_holder_name = account_holder_name
      self._account_balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self._account_balance += amount
          print(f"Deposited ${amount}. New balance: ${self._account_balance}")
      else:
          print("Invalid deposit amount. Please deposit a positive amount.")

  def withdraw(self, amount):
      if amount > 0 and amount <= self._account_balance:
          self._account_balance -= amount
          print(f"Withdrew ${amount}. New balance: ${self._account_balance}")
      elif amount <= 0:
          print("Invalid withdrawal amount. Please withdraw a positive amount.")
      else:
          print("Insufficient funds for withdrawal.")

  def display_balance(self):
      print(f"Account Balance for {self._account_holder_name}: ${self._account_balance}")

my_account = BankAccount("123456789", "John Doe", 1000)

my_account.display_balance()
my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(1500)