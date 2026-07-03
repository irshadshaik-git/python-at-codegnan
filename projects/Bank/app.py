#user table
user = {
        1234:{'name':"eeshu",'Email':"22x51a04811@gmail.com",'balance':500,"password":"1234"},
        1234:{'name':"bhai",'Email':"22x51a04811@gmail.com",'balance':1000,"password":"1234"},
        
        }

#services

def register(name:str,email:str,initial_deposite:int,password:str):
    pass

def login(account:int,password:str)->bool:
    pass


#balance function defination
def balance(account:int)->int:
    pass


#withdraw function defination
def withdraw(account:int,withdraw_amount:int)->str:
    pass


#diposite function Defination
def deposite(account:int,deposite_amount:int):
    pass


#transfer function defination
def transfer(sender:int,reciever:int,transfer_amount:int):
    pass



#Ministatement function defination
def ministament(account:int):
    pass


# logout function defination
def logout():
    pass


# main

if __name__=="__main__":

    print("welcome to the small scale bank")
    print("1.Register \n 2.Login")
    choice = int(input("seclect your choice:"))
    

    #calling rgister function
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
                
