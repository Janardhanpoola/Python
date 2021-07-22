class Bank:
    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath,"r") as file:
            self.amount=int(file.read())

    def withdraw(self,withdraw_amnt):
        self.amount=self.amount-withdraw_amnt
    
    def deposit(self,deposit):
        self.amount=self.amount-deposit

    def commit(self):
        with open(self.filepath,"w") as file:
            file.write(str(self.amount))

b1=Bank("banking.txt")
print(b1.amount)
b1.withdraw(800)
b1.commit()
print(b1.amount)
b1.deposit(346)
b1.commit()


