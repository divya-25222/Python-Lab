class Bank:
    def __init__(self,name,acc_no,bal=1000):     #Inizializer   (__Dunder method) 
        self.name= name                          #self.name = varibale    public variable
        self.acc_no = acc_no 
        self.__bal = bal                         #Private
        self.trans = []                          # nested form [['cr',2500]]

    def display(self):
        print('-'*30)
        print('BOB')
        print('-'*30)
        print(f'Holder Name : {self.name}')
        print(f'Account No : {self.acc_no}')
        print(f'Balance : Rs{self.__bal}')
        print('-'*30)

    def credit(self,cr_amt):
        self.bal = self.__bal + cr_amt
        print(f'Hey {self.name} amount credited Rs{cr_amt}')
        print(f'Total Balance Rs {self.__bal} ')
        self.trans.append(['cr',cr_amt])

    def debit(self,db_amt):
        if self.bal < db_amt:
            print('Insufficient Balance')
        else:
            self.bal = self.__bal - db_amt
            print(f'Hey {self.name} amount debited Rs{db_amt}')
            print(f'Total Balance Rs {self.__bal} ')
            self.trans.append(['db',db_amt])

    def passbook(self):
        print('-'*30)
        print('BOB')
        print('-'*30)
        print('S.No        Cr/Db          Amount')
        print('-'*30)
        i=1
        for a,b in self.trans:
            print(f'{i}        {a}             Rs {b}')
            i+=1
        print('-'*30)
        print(f'Total Balance Rs{self.bal}')
        print('-'*30)



#object
b1 = Bank('Divya Joshi',1001,10000)
b1.display()
b1.credit(2500)
b1.debit(200)
b1.passbook()
