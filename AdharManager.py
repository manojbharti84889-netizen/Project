Adhar_record={}
def add_adhar_record():
   name=input('Enter your name')
   adhar_num=int(input('Enter your adhar number'))
   dob=input('Enter your date of birth (DD-MM-YY)')
   address=input('Enter your address')
   Adhar_record[adhar_num]={"Name":name,
                            "DOB":dob,
                            "Address":address}
   print('Adhar record added successfully')
   
def view_adhar_record():
    for adhar_num, user_details in Adhar_record.items():
       print(f"Adhar number: {adhar_num}")
       for key, value in user_details.items():
          print(f"{key} : {value}")
          
def search_adhar():
    adhar_num=int(input('Enter your number:'))
    if adhar_num in Adhar_record:
       print(f"\nUser detail found to this adhar number:{adhar_num}")
       for key, value in Adhar_record[adhar_num].items():
          print(f"{key}: {value}")
    else:
       print('User details not found to this adhar number:',adhar_number)
       
def update_adhar_data():
   adhar_num=int(input('Enter your adhar number to update'))
   if adhar_num in Adhar_record:
      name=input('Enter your name')
      dob=input('Enter your date of birth (DD-MM-YY)')
      address=input('Enter your address')
      Adhar_record[adhar_num]={"Name":name,"DOB":dob,"Address":address}
      print('Adhar record updated successfully')
   else:
      print('Adhar number is not found')
      
def delete_adhar_record():
   adhar_num=int(input('Enter your adhar number for delete'))
   if adhar_num in Adhar_record:
      del Adhar_record[adhar_num]
      print('Adhar record deleted successfully')
      
def show_menu():
    print('1.Add adhar record\n2.View adhar record\n3.Search adhar by adhar number\n4.Update adhar data\n5.Delete adhar data')
    choice=int(input('Enter your option'))
    if choice==1:
       add_adhar_record()
    elif choice==2:
       view_adhar_record()
    elif choice==3:
       search_adhar()
    elif choice==4:
       update_adhar_data()
    elif choice==5:
       delete_adhar_record()
    else:
       print('Invalid choice')
             
while True:
   show_menu()
        
        

    
              

    
 


