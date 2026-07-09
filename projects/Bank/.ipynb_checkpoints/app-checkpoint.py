#user table
from balance import balance
from diposite import deposite
from login import login
from logout import logout
from mini_stament import ministament
from register import register
from transfer import transfer 
from withdraw import withdraw

user = {
        1234:{'name':"eeshu",'Email':"22x51a04811@gmail.com",'balance':500,"password":"1234"},
        1235:{'name':"bhai",'Email':"22x51a04811@gmail.com",'balance':1000,"password":"1235"},
        
        }

# main

if __name__=="__main__":

    print("welcome to the small scale bank")
    print("1.Register \n 2.Login")
    choice = int(input("seclect your choice:"))
    

    #calling register function
    if choice == 1:
        print("Register Page Under Development Process......")
    #calling Login Function
    elif choice == 2:
        account = int(input("Enter your account number: "))
        password = input("Enter your password: ")
        login_val = login(account=account,password=password)
        

        while login_val:
            print("The small scale Bank Providing services")
            print("1.Balance \n 2. Withdrawal \n 3.Diposite \n 4. Transfer \n 5.Ministatement \n 6.logout")
            choice = int(input("Enter your choice(1-6): "))

            if choice == 1:
                # call Balance function
                current_balance = balance(account=account)
                print(f"current balance is:{current_balance} ")
            
            
            
            elif choice == 2:
                amount = int(input("enter your withdraw amount: "))
                #call withdraw function
                res = withdraw(account=account, withdraw_amount=amount)
                print(res)


            elif choice == 3:
                amount = (int(input("Enter amount to deposit")))
                # call deposite function
                res=deposite(account=account,deposite_amount=amount)
                print(res)


            elif choice == 4:
                receiver = int(input())
                amount = int(input())
                # call transfer function
                res=transfer(sender=account,reciever= receiver,transfer_amount=amount)
                print(res)


            elif choice == 5:
                # call  ministamen :
                res= ministament(account=account)
                print(res)
                 
            else:
                 print("Enter the valid choice from 1 to 6")
        else:
            print("invalid cratantial")
                    
