class railway_ticket:
    def __init__(self):
        from_to_destinations={'hyderabad':['vijayawada',600,40],'secunderabad':['bheemavaram',500,35],'shamshabad':['tamilnadu',800,80]}
        persons=[]
        self.persons=persons
        self.from_to_destinations=from_to_destinations  
        print('tickets available')
        print(format('from','<30'),format('to','<30'),format('price','<30'),format('seats left','<30'))
        for i,j in from_to_destinations.items():
            print(format(i,'<30'),format(j[0],'<30'),format(j[1],'<30'),format(j[2],'<30'))
    def booking(self):
        while True:
            from_destination=input('enter from destination:')
            if from_destination in self.from_to_destinations:
                to_destination=input('enter to destination:')
                if self.from_to_destinations[from_destination][0]==to_destination:
                    no_of_tickets=int(input('please enter no of tickets:'))
                    if self.from_to_destinations[from_destination][2]>=no_of_tickets:
                        self.from_to_destinations[from_destination][2]=self.from_to_destinations[from_destination][2]-no_of_tickets
                        #print(self.from_to_destinations)
                        amount=self.from_to_destinations[from_destination][1]*no_of_tickets
                        for i in range(no_of_tickets):
                            name=input('enter person name:')
                            seats=random.randint(1,100)
                            print(i+1,name)
                            self.persons.append(name)
                            self.persons.append(seats)
                        print(self.persons)
                        print('Tickets price:{}/-'.format(amount))
                        acc_no=int(input('enter your account no:'))
                        if acc_no in credentials:
                            if credentials[acc_no][1]>=amount:
                                pin=int(input('enter your pin:'))
                                if credentials[acc_no][0]==pin:
                                    print('Transaction successfull')
                                    credentials[acc_no][1]=credentials[acc_no][1]-amount
                                    print('Tickets booked successfully')
                                    print('-'*7,'Ticket details','-'*7)
                                    print(from_destination,'-',to_destination)           
                                    if len(self.persons)>=1:
                                        for i in range(len(self.persons)):
                                            if i%2==0:
                                                print(format('name:','<7'),format(self.persons[i],'<7'),format('seat no:','<7'),format(self.persons[i+1],'<7'))         
                                        print('Amount paid ',amount,'/-',sep='')
                                        print('-'*7,'Happy Journey','-'*7)
                                        break
                                else:
                                    print('wrong pin entered')
                                    self.persons.clear()
                            else:
                                print('insufficient balance')
                                self.persons.clear()
                        else:
                            print('wrong account no')
                            self.persons.clear()
                    else:
                        print('{} seats left {} - {} you can check in tickets available section'.format(self.from_to_destinations[from_destination][2],from_destination,to_destination))
                        x1=eval(input('if you don want to buy tickets press-1 press any other key to buy'))
                        if x1==1:
                            print('logged out successfully')
                            break    
                else:
                    print(from_destination,'-',to_destination,'is not available please check tickets available section')
                    x1=input("if you dont want to buy tickets click 'n' if you want to buy press any other alphabet:")
                    if x1=='n':
                        print('logged out successfully')
                        break
            else:
                print('please check tickets available section')
                x1=input("if u dont want to buy tickets click 'n' if you want to buy press any other alphabet:")
                if x1=='n':
                    print('logged out successfully')
                    break                

import random
users={'naveen':'123','krishna':'456'}
credentials={902475:[3579,2000],902685:[7651,2500]}
#902475-acc no,3579-pin,2000-balance
username=input('enter username:')
if username in users:
    password=input('enter your password:')
    if password==users[username]:
        print('login successfull')
        x=railway_ticket()
        x.booking()
    else:
        print('wrong password')
elif username not in users:
    print('creating new IRCTC account')
    password1=input('enter your password:')
    users[username]=password1
    print('login successfull')
    x=railway_ticket()
    x.booking()