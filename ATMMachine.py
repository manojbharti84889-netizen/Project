import os
import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='atm'
    )
cursor=conn.cursor()
def register():
    name=input('Enter name:')
    pin=input('Enter pin:')
    try:
       query="INSERT INTO customer(pin,name,balance)VALUES(%s,%s,%s)"
       values=(pin,name,0)
       cursor.execute(query,values)
       conn.commit()
       filename=name+".txt"   
       with open(filename,"w") as f:
           f.write(f"name: {name}\n")
           f.write(f"pin: {pin}\n")
           f.write("balance: 0")
           print('Register successfully')
    except mysql.connector.IntegrityError as e:
        if "Duplicate entry" in str(e):
            print('❌❌ This account or pin already exists!')
        else:
            print('Database Error', e)
def balance_update(filename,name,pin,balance):
    with open(filename,"w") as f:
        f.write(f"name: {name}\n")
        f.write(f"pin: {pin}\n")
        f.write(f"balance: {balance}")
def login():                                                                                                 
     name=input('Enter name:')
     pin=input('Enter pin:')
     filename=name+".txt"
     if not os.path.exists(filename):
         print('Account not found! please check name or password')
        
     else:
        with open(filename,'r') as f:
                lines=f.readlines()
                saved_name=lines[0].split(':')[1].strip()
                saved_pin=lines[1].split(':')[1].strip()
                balance = float(lines[2].split(':')[1].strip())
                if name==saved_name and pin==saved_pin:
                    print('Login successfully')
                    def menu():
                       nonlocal balance
                       while True:
                          print('1.Check balance\n2.Credit amount\n3.Debit amount\n4.Exit')
                          choice=int(input('Enter your choice'))
                          if choice==1:
                              print(f"Current balance is: {balance}")
                          elif choice==2:
                               amt=int(input('Enter credit amount'))
                               balance+=amt
                               cursor.execute("UPDATE customer SET balance=%s WHERE pin=%s", (balance,pin))
                               conn.commit()
                               balance_update(filename,saved_name,saved_pin,balance)
                               print(f"Total balance: {balance}")
                          elif choice==3:
                             amt=float(input('Enter debit amount'))
                             if amt<balance:
                                balance-=amt
                                cursor.execute("UPDATE customer SET balance=%s WHERE pin=%s", (balance,pin))
                                conn.commit()
                                balance_update(filename,saved_name,saved_pin,balance)
                                print(f"Current amount: {balance}")
                             else:
                                print('Insufficient amount')
                          elif choice==4:
                            print('Exited and data saved successfully')
                            break                        
                    menu()
                else:
                   print('Name or Pin not match')
def data():
    while True:
       print('1.Register\n2.Login\n3.Exit')
       c=int(input('Enter your choice'))
       if c==1:
          register()
       elif c==2:
          login()
       elif c==3:
           print('Existed')
           break
data()


    
        




