class Account:
    def __init__(self):
        self.acctnumber = int(input("Enter the Account number: "))
        self.acctname = input("Enter the Account name: ")
        self.balance = int(input("Enter the balance: "))

    def withdraw(self):
        w_amount = int(input("Enter the withdraw amount: "))
        if (w_amount > self.balance):
            print("Insuffient Balance")
        else:
            self.balance = self.balance - w_amount
            self.showbalance()

    def deposit(self):
        d_amount=int(input("Enter the deposit amount: "))
        self.balance=self.balance+d_amount
        self.showbalance()

    def  showbalance(self):
        print("The current balance is",self.balance)





l=[]
while(True):
    print("1.Creat a new Account")
    print("2.Withdraw")
    print("3.Deposit")
    print("4.Show balance")
    print("5.Exit")

    ch=int(input("Enter the option: "))
    if ch == 1:
        a=Account()
        l.append(a)
        print(a)

    elif ch == 2:
        acctnum=int(input("Enter the account number: "))
        for i in l:
            if (i.acctnumber==acctnum):
                i.withdraw()
                break
        else:
            print("Account does not exist")

    elif ch == 3:
        acctnum = int(input("Enter the account number: "))
        for i in l:
            if (i.acctnumber==acctnum):
                i.deposit()
                break
        else:
            print("Account does not exist")

    elif ch == 4:
        acctnum = int(input("Enter the account number"))
        for i in l:
            if (i.acctnumber == acctnum):
                i.showbalance()

    else:
        exit()