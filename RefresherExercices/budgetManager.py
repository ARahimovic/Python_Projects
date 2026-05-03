class Account:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self,amount):
        if(self._balance - amount < 0):
            print("Insufficient Funds")
            return 
        self._balance -= amount

    def __str__(self):
       return f"Account name : {self._owner}\nAccount balance : {self._balance}"


if __name__ == "__main__":
    myAccount = Account("Rahimovic", 6500)
    myAccount.deposit(3200)

    print(myAccount)

    myAccount.withdraw(10000)
    myAccount.withdraw(4000)
    print(myAccount)
 
        