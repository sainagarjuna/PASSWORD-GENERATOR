print("enter your 12 character password:")
print("""Password must contain atleast 1 upper case letter,lower case letter,special symbol and number""")

special_symbol=["@","#","*","!"]
x=input() #password

if(len(x)<12):
    print("enter a strong password")


if not any(i.isdigit() for i in x):
    print("password must contain atleast one digit")

if not any(i.isupper() for i in x):
    print("password must contain atleast one upper case letter")

if not any(i.islower() for i in x):
    print("password must contain atleast one lower case letter")

if not any(i in special_symbol for i in x):
    print("passowrd must contain aleast one special symbol")

else:
    print("password created\n\n")
    
    print("for any changes in passwordSai@2020156889")
    print("""1.check password
2.update password
3.exit\n""")

    user_in=int(input("enter your requirement:"))

    while(user_in<4):
        if(user_in==1):
            now=input("enter your password to check whether correct or wrong:")
            if(x==now):
                print("correct!!")
                print(f"your password is {x}")
                
            else:
                print("wrong password")
                
        if(user_in==2):
            print("enter new password:")
            y=input()
            if(len(y)<12):
                print("enter a strong password!")
            if not any(i.isdigit() for i in y):
                print("password must contain atleast one digit")
            if not any(i.isupper() for i in y):
                print("password must contain atleast one upper case letter")
            if not any(i.islower() for i in y):
                print("password must contain atleast one lower case letter")
            if not any(i in special_symbol for i in y):
                print("passowrd must contain aleast one special symbol")
            else:
                print("password updated!")
                

                
        if(user_in==3):
            print("successfuly done!")
            break
        else:
            print("enter number b/w 1 to 3")
        user_in=int(input("enter your requirement:"))
        
    

    
    
    
      
      
