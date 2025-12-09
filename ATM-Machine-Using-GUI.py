import pygame
from tkinter import *
from tkinter import ttk, messagebox
import os
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\HP\Downloads\WhatsApp Audio 2025-11-27 at 20.41.00_fbcc2209.mp3")
pygame.mixer.music.play()
root=Tk()
root.configure(bg='lightblue')
root.geometry("300x200")

saved_name=""
saved_pin=""
def Third_window():
        global variable
        boot=Toplevel(root)
        boot.configure(bg='#222222')
        boot.title('ATM')
        boot.geometry("300x200")
        amountvalue=IntVar()
        debitvalue=IntVar()
        def show_balance():
              global saved_balance,filename
              with open(filename, 'r') as f:
                   lines = f.readlines()
                   saved_balance = float(lines[2].split(':')[1].strip())
                   messagebox.showinfo("",f"Current balance: {saved_balance}")
        def credit_amount():
              global saved_balance,filename
              with open(filename, 'r') as f:
                   lines = f.readlines()
                   saved_balance = float(lines[2].split(':')[1].strip())
                   saved_balance+=amountvalue.get()
                   messagebox.showinfo("",f"Total amount: {saved_balance}")
                   with open(filename, 'w') as f:
                        f.write(f"name: {saved_name}\n")
                        f.write(f"pin: {saved_pin}\n")   
                        f.write(f"balance: {saved_balance}")
        def debit_amount():
                global saved_balance,filename
                with open(filename, 'r') as f:
                   lines = f.readlines()
                   saved_balance = float(lines[2].split(':')[1].strip())
                if debitvalue.get() > saved_balance:
                       messagebox.showinfo("",f"Insufficient balance!")
                else:    
                    saved_balance-=debitvalue.get()
                    messagebox.showinfo("",f"Remaining balance: {saved_balance}")
                    with open(filename, 'w') as f:
                        f.write(f"name: {saved_name}\n")
                        f.write(f"pin: {saved_pin}\n")   
                        f.write(f"balance: {saved_balance}")
        Button(boot,text='Check balance',bg='pink',fg='black',command=show_balance).grid(row=0,column=0)
        amount_entry=Label(boot,text='Credit amount:')
        amount_entry.grid(row=1,column=0)
        balance_entry=Entry(boot,textvariable=amountvalue)
        balance_entry.grid(row=1,column=1)
        Button(boot,text='Press',bg='pink',fg='black',command=credit_amount).grid(row=2,column=0)
        
        amount_entry1=Label(boot,text='Debit amount:')
        amount_entry1.grid(row=3,column=0)
        balance_entry1=Entry(boot,textvariable=debitvalue)
        balance_entry1.grid(row=3,column=1)
        Button(boot,text='Press',bg='pink',fg='black',command=debit_amount).grid(row=4,column=0)
        Button(boot,text='Exit',bg='pink',fg='black',width=11,height=1,command=quit).grid(row=5,column=0)
def verify():
    global filename,saved_pin,saved_name,saved_balance
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            saved_name = lines[0].split(':')[1].strip() 
            saved_pin = lines[1].split(':')[1].strip()
            saved_balance = float(lines[2].split(':')[1].strip())
            if e.get().strip() == saved_pin:
                    
                Third_window()
            else:
                messagebox.showinfo("", "Pin does not match")

    except:
        messagebox.showinfo("", "User file not found")

def second_window():
        global filename
        filename=namevalue.get()+".txt"
        if os.path.exists(filename):
                messagebox.showinfo("", "Account aready exit please use fullname or yourname123")
        else:        
            with open(filename,"w") as f:
                f.write(f"name: {namevalue.get()}\n")
                f.write(f"pin: {pinvalue.get()}\n")
                f.write(f"balance: {0}")
                pygame.mixer.init()
                pygame.mixer.music.load(r"C:\Users\HP\Downloads\WhatsApp Audio 2025-11-27 at 20.40.48_aea7f701.mp3")
                pygame.mixer.music.play()
                loot=Toplevel(root)
                loot.configure(bg='brown')
                loot.title('Login')
                loot.geometry("300x200")
                global e
                e = Entry(loot, width=20,font=('Arial', 20),show='*')
                e.grid(row=0, column=0, columnspan=4)
                Button(loot,text='7',bg='grey',width=5,height=2,command=lambda:e.insert(END,'7')).grid(row=1,column=0)
                Button(loot,text='8',bg='grey',width=5,height=2,command=lambda:e.insert(END,'8')).grid(row=1,column=1)
                Button(loot,text='9',bg='grey',width=5,height=2,command=lambda:e.insert(END,'9')).grid(row=1,column=2)
                Button(loot,text='4',bg='grey',width=5,height=2,command=lambda:e.insert(END,'4')).grid(row=1,column=3)
                Button(loot,text='5',bg='grey',width=5,height=2,command=lambda:e.insert(END,'5')).grid(row=2,column=0)
                Button(loot,text='6',bg='grey',width=5,height=2,command=lambda:e.insert(END,'6')).grid(row=2,column=1)
                Button(loot,text='1',bg='grey',width=5,height=2,command=lambda:e.insert(END,'1')).grid(row=2,column=2)
                Button(loot,text='2',bg='grey',width=5,height=2,command=lambda:e.insert(END,'2')).grid(row=2,column=3)
                Button(loot,text='3',bg='grey',width=5,height=2,command=lambda:e.insert(END,'3')).grid(row=3,column=0)
                Button(loot,text='0',bg='grey',width=5,height=2,command=lambda:e.insert(END,'0')).grid(row=3,column=1)
                Button(loot,text='Enter',bg='grey',width=10,height=2,command=verify).grid(row=3,column=2)
def login_window():
    global filename
    filename = name1value.get() + ".txt"
    if not os.path.exists(filename):
        messagebox.showinfo("", "Account not found!")
    else:    
                pygame.mixer.init()
                pygame.mixer.music.load(r"C:\Users\HP\Downloads\WhatsApp Audio 2025-11-27 at 20.40.48_aea7f701.mp3")
                pygame.mixer.music.play()
           
                poot = Toplevel(root)
                poot.configure(bg='brown')
                poot.title("Login")
                poot.geometry("300x200")
                global e
                e = Entry(poot, width=20, font=('Arial', 20), show='*')
                e.grid(row=0, column=0, columnspan=4)
                Button(poot,text='7',bg='grey',width=5,height=2,command=lambda:e.insert(END,'7')).grid(row=1,column=0)
                Button(poot,text='8',bg='grey',width=5,height=2,command=lambda:e.insert(END,'8')).grid(row=1,column=1)
                Button(poot,text='9',bg='grey',width=5,height=2,command=lambda:e.insert(END,'9')).grid(row=1,column=2)
                Button(poot,text='4',bg='grey',width=5,height=2,command=lambda:e.insert(END,'4')).grid(row=1,column=3)
                Button(poot,text='5',bg='grey',width=5,height=2,command=lambda:e.insert(END,'5')).grid(row=2,column=0)
                Button(poot,text='6',bg='grey',width=5,height=2,command=lambda:e.insert(END,'6')).grid(row=2,column=1)
                Button(poot,text='1',bg='grey',width=5,height=2,command=lambda:e.insert(END,'1')).grid(row=2,column=2)
                Button(poot,text='2',bg='grey',width=5,height=2,command=lambda:e.insert(END,'2')).grid(row=2,column=3)
                Button(poot,text='3',bg='grey',width=5,height=2,command=lambda:e.insert(END,'3')).grid(row=3,column=0)
                Button(poot,text='0',bg='grey',width=5,height=2,command=lambda:e.insert(END,'0')).grid(row=3,column=1)
                Button(poot,text='Enter',bg='grey',width=10,height=2,command=verify).grid(row=3,column=2)

Label(root,text='Registration for new user',bg='#222222',fg='white').grid(row=0,column=0)
name=Label(root,text='Enter your name:')
name.grid(row=1,column=0)
namevalue=StringVar()
pinvalue=StringVar()
nameentry=Entry(root,textvariable=namevalue)
nameentry.grid(row=1,column=1)
pinentry=Entry(root,textvariable=pinvalue,show='*')
pinentry.grid(row=2,column=1)
pin=Label(root,text='Set your 4 digit PIN:')
pin.grid(row=2,column=0)
Button(root,text='Submit',bg='red',command=second_window).grid(row=3,column=0)
Label(root,text='Press verify if aready account',bg='#222222',fg='white').grid(row=4,column=0)
name1=Label(root,text='Enter your name:')
name1.grid(row=5,column=0)
name1value=StringVar()
nameentry1=Entry(root,textvariable=name1value)
nameentry1.grid(row=5,column=1)
Button(root,text='verify',bg='red',command=login_window).grid(row=6,column=0)
root.mainloop()


    
 
