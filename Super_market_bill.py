#super market bill
name=input('enter your name:')
loc=input('enter your address:')
c={'sugar':40,'maggi':50,'boost':30,'colgate':40,'paneer':110,'salt':20,'oil':220}
print('available items')
print(format('items','<19'),format('price','<19'))
for i,j in c.items():
    if i=='oil':
        print(format(i,'<20'),j,'/ltr',sep='')
    else:
        print(format(i,'<20'),j,'/kg',sep='')
d={}
while True:
    x=int(input("if you want buy press1 or press2 for exit press any other integer for billing:"))
    if x==1:
        item=input('enter your items:')
        if item in (c and d):
            print('please select another item')
            x1=input('do you want to update quantity of item or change item (quantity/item) (press any other key(string) for no):')
            if x1=='quantity':
                x2=int(input('please enter quantity of item:'))
                d[item]=c[item]*x2
                print(d)
                print('quantity of item is updated')
            elif x1=='item':
                d.pop(item)
                x3=input('please  add new item:')
                if x3 in (c and d):
                    print('please select another item')
                        
                elif (x3 in c) and (x3 not in d):
                    x4=int(input('enter quantity:'))
                    d[x3]=c[x3]*x4
                    print(d)
                else:
                    print('please select items we have in market')
            else:
                print('sorry i dont want to update or change any item or quantity')
                print(d)
        elif (item in c) and (item not in d):
            q=int(input('enter quantity:'))
            d[item]=c[item]*q
            print(d)
        else:
            print('please select  items we have in the market')
    elif x==2:   
        if len(d)>=1:
            sel_items=input("do you want to buy selected items click 'y' for yes click any other for 'no'")
            if sel_items=='y':
                print('-'*40,'Bill','-'*40)
                print(' '*40,'Dmart',' '*39)
                print('Name:',name)
                print('Address:',loc)
                print()
                print(format('sno','<21'),format('Item','<21'),format('Qty','<21'),format('price','<21'))
                cd=0
                cd1=0
                for i,j in d.items():
                    cd=cd+1
                    cd1 +=j
                    print(format(cd,'<21'),format(i,'21'),format(int(j/c[i]),'<21'),format(j,'<21'))
                print(' '*59,'Total',format(cd1,'<3'))
                print('-'*30,'Thank you visit again','-'*31)
                break
            else:
                d.clear()
                break
        else:
            break
    else:
        if len(d)>=1:
            print('-'*40,'Bill','-'*40)
            print(' '*40,'Dmart',' '*39)
            print('Name:',name)
            print('Address:',loc)
            print()
            print(format('sno','<21'),format('Item','<21'),format('Qty','<21'),format('price','<21'))
            ab=0
            ab1=0
            for i,j in d.items():
                ab=ab+1
                ab1 +=j
                print(format(ab,'<21'),format(i,'<21'),format(int(j/c[i]),'<21'),format(j,'<21'))
            print(' '*59,'Total',format(ab1,'<3'))
            print('-'*30,'Thank you visit again','-'*31)
            break
        elif len(d)==0:
            print('your bag is empty please select items to buy')
         

            
    

    






