class Bank():
    def __init__(self):
        Transactions=[]#for ministatement
        if sign_in in credentials:
            Transactions.append(credentials[sign_in][1])
        self.Transactions=Transactions
    def create_account(self):
        name=input('enter your name:')
        Aadhar_no=int(input('enter your 12 digit Aadhar no:'))
        pan_no=input('enter your 10charcters pan no:')
        if len(str(Aadhar_no))==12 and len(pan_no)==10:
            try:
                for i in kyc_details.values():
                        if Aadhar_no!=i[1] and pan_no!=i[2]:
                            account_no=random.randint(902000,902300)
                            print('your account no:',account_no)
                            password=int(input('enter 4 digit pin to secure your account:'))
                            print('your account_details and pin is confidential dont share with anyone')
                            account_balance=0
                            kyc_details[account_no]=[name,Aadhar_no,pan_no]
                            credentials[account_no]=[password,account_balance,name]
                            print(kyc_details)
                            print(credentials)
                        else:
                            print('your details already in use')
            except:
                print('your account created successfully')
        else:
            print('wrong details entered')
    def deposit(self):
        for i in credentials:
            if i==sign_in:
                print('current balance',self.Transactions[-1])
                amount=int(input('enter amount to deposit:'))
                credentials[i][1]=credentials[i][1]+amount
                self.Transactions.append(credentials[i][1])
                #print(self.Transactions)
                #print(credentials)
                print('amount credited successfully updated balance is',credentials[i][1])
    def withdraw(self):
        for i in credentials:
            if i==sign_in:
                print('current balance',self.Transactions[-1])
                Amount=int(input('enter amount to withdraw:'))
                if credentials[i][1]>=Amount:
                    credentials[i][1]=credentials[i][1]-Amount
                    self.Transactions.append(credentials[i][1])
                    print('{} withdrawn successfully updated balance is {}'.format(Amount,credentials[i][1]))
                else:
                    print('Insufficient balance',credentials[i][1])
    def transfer(self):
        for i in credentials:
            if i==sign_in:
                print('current balance',self.Transactions[-1])
                Acc_no=int(input('Enter account number to transfer:'))
                if (Acc_no in credentials) and (sign_in!=Acc_no):
                    pay=int(input('enter amount to transfer:'))
                    if credentials[i][1]>=pay:
                        credentials[i][1]=credentials[i][1]-pay
                        self.Transactions.append(credentials[i][1])
                        credentials[Acc_no][1]=credentials[Acc_no][1]+pay
                        print('Transaction of {} to {} is successfull'.format(pay,Acc_no))
                        print('updated balance is',credentials[i][1])
                    else:
                        print('Insufficient balance',credentials[i][1])
                elif sign_in==Acc_no:
                    print('cannot transfer to same acount')
                else:
                    print('account no not found')
    def mini_statement(self):
        if len(self.Transactions)>1:
            print('initial balance is',self.Transactions[0])
            for i in range(len(self.Transactions)):
                try:
                    if self.Transactions[i]<self.Transactions[i+1]:
                        print('Credited Amount',self.Transactions[i+1]-self.Transactions[i])
                    else:
                        print('Debited amount',self.Transactions[i]-self.Transactions[i+1])
                except IndexError:
                    print('final balance',self.Transactions[i])
        else:
            print('no transactions done yet your balance is',self.Transactions[0])
import random
credentials={902475:[3579,2000,'naveen'],902685:[7651,2500,'krishna']}
#90245-AccNo,3579-PIN,2000-Account balance
kyc_details={902475:['naveen',345623179024,'hjafa200z'],902685:['krishna',265715382913,'fsdqr100a']}
#345623179024-Aadhaar No ,hjafa200z-Pan no
sign_in=int(input('enter your account no:'))
if sign_in in credentials:
    pin=int(input('enter your pin:'))
    if credentials[sign_in][0]==pin:
        print('login successfull')
        x=Bank()
        while True:
            options=eval(input('enter 1-deposit 2-withdraw 3-transfer 4-ministatement press any other key to logout:'))
            if options==1:
                x.deposit()
            elif options==2:
                x.withdraw()
            elif options==3:
                x.transfer()
            elif options==4:
                x.mini_statement()
            else:
                print('logged out successfully')
                break
    else :
        print('wrong pin entered')
elif sign_in not in credentials:
    new=input('wrong account no do you want to create account in bank y/n:')
    if new=='y':
        x=Bank()
        x.create_account()
        sign_in=int(input('enter your account no:'))
        if sign_in in credentials:
            pin=int(input('enter your pin:'))
            if credentials[sign_in][0]==pin:
                print('login successfull')
                x=Bank()
                while True:
                    options=eval(input('enter 1-deposit 2-withdraw 3-transfer 4-ministatement press any other key to logout:'))
                    if options==1:
                        x.deposit()
                    elif options==2:
                        x.withdraw()
                    elif options==3:
                        x.transfer()
                    elif options==4:
                        x.mini_statement()
                    else:
                        print('logged out successfully')
                        break
            else :
                print('wrong pin entered')
    else:
        print('exit')

