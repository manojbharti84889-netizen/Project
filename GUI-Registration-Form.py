from tkinter import *
from tkinter import ttk, messagebox

root=Tk()
root.title('Registration Form')
root.geometry("455x344")
def getvalue():
    if agree.get()==1:
       selected = combo.get()
       combobox.set(selected)  
       print(f"Name: {namevalue.get()},Age: {agevalue.get()},date: {datevalue.get()},Qualification: {quilvalue.get()},Mail ID: {emailvalue.get()},Address: {addvalue.get()},Password: {passwordvalue.get()},Gender: {radio.get()},State: {combobox.get()}")
       with open("oo.txt","a") as f:
          f.write(f"Name: {namevalue.get()},Age: {agevalue.get()},date: {datevalue.get()},Qualification: {quilvalue.get()},Mail ID: {emailvalue.get()},Address: {addvalue.get()},Password: {passwordvalue.get()},Gender: {radio.get()},State: {combobox.get()}\n")
          messagebox.showinfo("","Form submitted successfully")
    else:
        messagebox.showinfo("","please choose on the agree button!")
name=Label(root,text='Name:')
name.grid(row=0,column=0)
age=Label(root,text='Age:' )
age.grid(row=1,column=0)
date=Label(root,text='Date(DD/MM/YY):')
date.grid(row=2,column=0)
label=Label(root,text='Gender:')
label.grid(row=3,column=0)
quil=Label(root,text='Quilification:')
quil.grid(row=4,column=0)
email=Label(root,text='MailID:')
email.grid(row=5,column=0)
add=Label(root,text='Address:')
add.grid(row=6,column=0)
password=Label(root,text='Set Password:')
password.grid(row=7,column=0)
state=Label(root,text='State:')
state.grid(row=8,column=0)

namevalue=StringVar()
agevalue=StringVar()
datevalue=StringVar()
quilvalue=StringVar()
emailvalue=StringVar()
addvalue=StringVar()
passwordvalue=StringVar()
#statevalue=StringVar()
radio=StringVar()
combobox=StringVar()
agree=IntVar()

nameentry=Entry(root,textvariable=namevalue)
nameentry.grid(row=0,column=1)
ageentry=Entry(root,textvariable=agevalue)
ageentry.grid(row=1,column=1)
dateentry=Entry(root,textvariable=datevalue)
dateentry.grid(row=2,column=1)
#radio Button
r=Radiobutton(root,text='M',variable=radio,value='M')
r.grid(row=3,column=1,sticky='w')
r1=Radiobutton(root,text='F',variable=radio,value='F')
r1.grid(row=3,column=1)
r2=Radiobutton(root,text='Other',variable=radio,value='Other')
r2.grid(row=3,column=1,sticky='e')

quilentry=Entry(root,textvariable=quilvalue)
quilentry.grid(row=4,column=1)
emailentry=Entry(root,textvariable=emailvalue)
emailentry.grid(row=5,column=1)
addentry=Entry(root,textvariable=addvalue)
addentry.grid(row=6,column=1)
passwordentry=Entry(root,textvariable=passwordvalue,show='*')
passwordentry.grid(row=7,column=1)
#Dropdown menu
states = ["Punjab", "maharashtra", "Bihar", "Utter Pradesh", "Gujrat","Rajesthan"]
combo = ttk.Combobox(root, values=states)
combo.grid(row=8,column=1)
combo.set("Select State:")  


b=Checkbutton(root,text='Do you agree this form',bg='red',variable=agree).grid(row=9,column=1)
Button(root,text='Submit',bg='pink',command=getvalue).grid(row=10,column=1)

root.mainloop()          
