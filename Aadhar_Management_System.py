record=[]
def add_adhar_data():
    name=input('Enter your name:')
    adhar_num=int(input('Enter your adhar number:'))
    dob=input('Enter your date of birth(DD/MM/YY):')
    address=input('Enter your address:')
    record.append([name,adhar_num,dob,address])          
    print('Adhar record added successfully')
    print('-------------------------------')

def fetch_data():
     for x in record:
          print("Name:", x[0],"\nAdhar number:", x[1],"\nDOB:", x[2],"\nAddress:", x[3])
          print('---------------------------')
         
def data_search_by_number():
    adhar_num=int(input('Enter your adhar number:'))
    for x in record:
        if x[1]==adhar_num:
            print("Name:", x[0],"\nDOB:", x[2],"\nAddress:", x[3])
            print('-----------------------------------')
            break
    else:
        print(f"Adhar data not found to this number:{adhar_num}")
def update_adhar():
    adhar_num=int(input('Enter your adhar number:'))
    for x in record:
        if x[1]==adhar_num:
            name=input('Enter your name:')
            dob=input('Enter your date of birth(DD/MM/YY):')
            address=input('Enter your address:')
            x[0]=name
            x[1]=adhar_num
            x[2]=dob
            x[3]=address
            print('Adhar data updated successfully:')
            print('--------------------------------')
            break
    else:
       print(f"Adhar data not found to this number:{adhar_num}")
def delete_data():
    adhar_num=int(input('Enter your adhar number:'))
    for x in record:
       if x[1]==adhar_num:
          record.remove(x)
          print('Adhar data deleted successfully')
       else:
          print('Adhar data not found!')
          print('----------------------')
def show_menu():
   while True:  
     print('1.Add data\n2.Fetch data\n3.Search data\n4.Update data\n5.Delete data\n6.Exit')
     choice=int(input('Enter your choice'))
     if choice==1:
        add_adhar_data()
     elif choice==2:
        fetch_data()
     elif choice==3:
        data_search_by_number()
     elif choice==4:
        update_adhar()
     elif choice==5:
        delete_data()
     elif choice==6:
        print('Existed')
        break
             
show_menu()       
    
            
    

    
    
    
