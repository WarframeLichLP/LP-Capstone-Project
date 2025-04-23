"""
Data Structures
Student Project
Project Title:
"""
##- Need to insert the  JSON Placeholder API-##

import random
import requests
import pp
url = "https://jsonplaceholder.typicode.com/users"
response1 = requests.get(url)
response2 = response1.json()
family = []


for filename in response2[:4]:
    family.append(filename["name"].split(" ")[0])
    random.shuffle(family)
    


    
    



money = [157, 180, 175, 200]
new_family_amount = 0

### -- Sign-in page (the "LiLaLo" means Live, Laugh, Love: the Karen motto -- ###
username = "FacebookLiLaLo23"
password = "AOLEnjoyer"

while 1 == 1:
    userinput = input("Please enter your username: ")
    passinput = input("Please enter your password: ")
    
    if passinput == password and userinput == username:
        print("Logging in...")
        

## -- the Welcome page -- ##

        print("Welcome back to the Family Bank app!")

## -- Main Loop -- ##
        while 2 == 2:
            
            

            app = input("Input 'withdraw' to withdraw money from a member's account, 'insert' to give money to a member's account, 'add' to add a member, or 'exit' to logout: ").lower()
            
        ## -- logout -- ##

            if app == "logout" or app == "exit":
                print("Logging out...")
                print()
                break

    ## -- Using a member's money -- ##

            if app == "withdraw":
                member_id = input("Enter the name of the member you will withdraw money from - " + str(family) + ": ")

        ## -- Name check -- ##


            
                if member_id not in family:
                    print("Invalid member.")
                    continue
        
        ## -- Indexing for the member and their money -- ##

                family_pos = family.index(member_id)
        
                member_amount = money[family_pos]
        
    

                print("You have $" + str(member_amount) + " within this account.")
                account_withdrawal = int(input("How much would you like to withdraw? $"))
            ## -- making sure the member has the desired withdrawal amount -- ##
        
        
                if member_amount > account_withdrawal:
                    new_member_amount = member_amount - account_withdrawal 
                    print("This member now owns $" + str(new_member_amount) + ".")
                    money[family_pos] = new_member_amount

            
    


        ## - notiofication for when a member has no money left - ##

                elif account_withdrawal == member_amount:
                    print("There is no money left on this member's account. Return to the homepage to add more money to it.")
                    new_member_amount = member_amount - account_withdrawal 
                    money[family_pos] = new_member_amount

            ## - Invalid input - ##

                elif member_amount < account_withdrawal:
                    print("This account does not have enough funds for that withdrawal.")

            ## - Adding money to a user's account - ##

            if app == "insert":
                member_id = input("Enter the name of the member you will insert money for - " + str(family) + ": ")


                if member_id not in family:
                    print("Invalid member.")
                    continue
            
                
                family_pos = family.index(member_id)
        
                member_amount = money[family_pos]
            
            
            
                print("You have $" + str(member_amount) + " within this account.")
                account_insert = int(input("How much would you like to insert? $"))
                new_member_amount = member_amount + account_insert 
                
                print("This member now owns $" + str(new_member_amount) + ".")
                money[family_pos] = new_member_amount

                
        ## -- Adding a member to the shared family account -- ##

            if app == "add":
                newmember = input("Enter the name of the member you would like to add: ")
        
        
            ## -- checks if name is already in use -- ##

                if newmember in family:
                    print("You are already using this name for a different member.")
                    continue


        ## -- Add family member to conjoined bank -- ##
                family.append(newmember)
                money.append(5)
                print("A new member has been added with the name " + newmember + " and a balance of $5.")
                print()


        
    else:
        print("Invalid username or password.")
        print()
        continue