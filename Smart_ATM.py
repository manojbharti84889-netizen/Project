import random
import time
pin = 8080
balance = 50000
max_attempts = 0

while max_attempts < 3:
    upin = int(input("Enter your PIN: "))
    if upin == pin:
        print("Welcome to HDFC bank")
        while True:
            print("1. Check Balance")
            print("2. Debit amount")
            print("3. Credit amount")
            print("4. Change PIN")
            print("5. Check Loan Eligibility")
            print("6. Exit")
            choice = int(input("Choose option (1-5): "))
            if choice == 1:
                print("Balance:", balance)
            elif choice == 2:
                amount = int(input("Enter amount to debit: "))
                if amount <= balance:
                   balance -= amount
                   print("Debited:", amount)
                   print("New Balance:", balance)
                else:
                   print("Insufficient Balance")
            elif choice == 3:
                amount = int(input("Enter amount to credit: "))
                balance += amount
                print("Credited:", amount)
                print("New Balance:", balance)
           
            elif choice == 4:
                mob=int(input('Enter your phone number linked by account:'))
                old_pin=int(input('Enter your old PIN:'))
                if old_pin==pin:
                    num=random.randint(1000,9000)
                    print('Your OTP:',num)
                    start=time.time()
                    print('You have only 10 second to enter the OTP:')
                    otp=int(input('Enter your received OTP:'))
                    end=time.time()
                    close=end - start
                    if close>10:
                        print('Time out! try again later')
                        break
                    if otp==num:              
                       new_pin=int(input('Enter your new PIN'))
                       print('New pin created successfully')
                    else:
                        print('Wrong OTP! Please check your received OTP')
                        break
                else:
                    print('Old PIN is incorrect! please enter right PIN')
                    break
        
            elif choice == 5:
                salary=int(input('Enter your salary'))
                age=int(input('Enter your age'))
                if salary >= 50000 and age >= 18:
                    print("You are eligible for the loan. please wait some days we send you information")
                else:
                       print("You are not eligible for the loan")
            elif choice == 6:
                print("Exited")
                break
            else:
                print("Invalid choice!")
        break
    else:
        print("Wrong PIN")
        max_attempts += 1
        if max_attempts == 3:
            print("Wait! you are enter 3 times wrong PIN your ATM card is block for 24 Hours")

    

