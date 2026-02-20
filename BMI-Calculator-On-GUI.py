from tkinter import*
from tkinter import ttk, messagebox

def bmi():
   try:
      sqr=(int(heightvalue.get())/100)*(int(heightvalue.get())/100)
      bmi=int(weightvalue.get())/sqr
      messagebox.showinfo("MBI",f"Your Body's BMI: {bmi}")
   except:
       messagebox.showinfo("Value Error!","Please enter only numerical value")
root=Tk()
root.title('BMI Calculator')
root.geometry("367x559")
root.configure(bg='floral white')
frame=Frame(root,bg='LightPink4',padx=20, pady=20)
frame.grid(row=0,column=0,padx=12,pady=10)
Label(frame,text='Welcome To BMI',font=('Segoe UI',16,'bold'),fg='white',bg='LightPink4').grid(row=0,column=0,padx=64)
weight=Label(root,text='Enter Your Weight:',bg='LightPink4',fg='white',font=(10)).grid(row=1,column=0)
weightvalue=StringVar()
weightentry=Entry(root,textvariable=weightvalue,width=22).grid(row=2,column=0)

height=Label(root,text='Enter Your Height(Centimeter):',bg='LightPink4',fg='white',font=(10)).grid(row=3,column=0)
heightvalue=StringVar()
heightentry=Entry(root,textvariable=heightvalue,width=22).grid(row=4,column=0)
Button(root,text='Check BMI',bg='misty rose',activebackground='white',command=bmi,width=18).grid(row=5,column=0)

def health_type():
   try:
      if int(BMIvalue.get())<18:
          messagebox.showinfo("","You Are UnderWeight")
      elif int(BMIvalue.get())>=18 and int(BMIvalue.get())<25:
          messagebox.showinfo("","You Are HealthWeight")
      elif int(BMIvalue.get())>=25 and int(BMIvalue.get())<30:
          messagebox.showinfo("","You Are OverWeight")
      else:
          messagebox.showinfo("","You Are Obese")
   except:
       messagebox.showinfo("Value Error!","Please enter only numerical value")
frame=Frame(root,bg='LightPink4',padx=20, pady=20)
frame.grid(row=6,column=0,padx=12,pady=10)
Label(frame,text='Check Health Type',font=('Arial',16,'bold'),fg='white',bg='LightPink4').grid(row=7,column=0,padx=55)
BMI=Label(root,text='Enter Your BMI:',bg='LightPink4',fg='white',font=(10),width=14).grid(row=8,column=0)
BMIvalue=StringVar()
BMIentry=Entry(root,textvariable=BMIvalue,width=22).grid(row=9,column=0)
Button(root,text='Check Health Type:',bg='misty rose',command=health_type,width=18,activebackground='white').grid(row=10,column=0)

def suggest_diet():
   selected = combo.get()
   combobox.set(selected)
   if combobox.get()=="UnderWeight":
       messagebox.showinfo("","You need to this type of diet-> High-Calarie, Nutrient-Dense Food")
   elif combobox.get()=="HealthWeight":
       messagebox.showinfo("","You need to this type of diet-> Hole Grain(Oats), Cup Of Fruits, Lean Proteins (Chicken,Fish,Paneer) ")
   elif combobox.get()=="OverWeight":
       messagebox.showinfo("","You need to this type of diet-> 9AM 1 Serving Max Protein Muesli With Milk, 11AM Green Tea , 1PM Salad+Multi Grain Roti, 4PM Green Tea Nuts  ")
   elif combobox.get()=="Obese":
       messagebox.showinfo("","You need to this type of diet-> Morning-Seeds Cocktail+Mixed Nuts, Mid Morning-Amla Drink Or Lemon Water, Evening-Green Tea And Black Chana Sundal")
   else:
       messagebox.showinfo("","Invalid Health Choice")
       
frame=Frame(root,bg='LightPink4',padx=20, pady=20)
frame.grid(row=11,column=0,padx=12,pady=10)
Label(frame,text='Suggest Diet Plale',font=('Arial',16,'bold'),fg='white',bg='LightPink4').grid(row=12,column=0,padx=55)
com=Label(root,text='Choose Your Health:',bg='LightPink4',fg='white',font=(10),width=15).grid(row=13,column=0)
diet = ["UnderWeight", "HealthWeight", "OverWeight", "Obese"]
combo = ttk.Combobox(root, values=diet)
combo.grid(row=14,column=0)
combo.set("Choose:") 
combobox=StringVar()
Button(root,text='Check Diet Plae:',bg='misty rose',command=suggest_diet,width=19,activebackground='white').grid(row=15,column=0)

def restart_app():
   weightvalue.set("")
   heightvalue.set("")
   BMIvalue.set("")
   combobox.set("")
Button(root,text='Restart:',bg='misty rose',command=restart_app,width=19,activebackground='white').grid(row=16,column=0)
   
root.mainloop()

           






