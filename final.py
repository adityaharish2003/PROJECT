__author__ = "Aditya Harish"
#new log
import getpass
import os
username = []
passwords = []
tries = 0 
def command_help():
    print("To make a new entry press N ")
    print("To view existing log , press L")
    print("To edit existing log , press E")
    print("To login to website , press LG")
    print("To quit , press Q")
    print("To delete an existing log , press D")
    print("To perform a search , press S")
    print("To view commands , press 'help' ")
while tries < 3:
    passwrd = getpass.getpass()
    if passwrd == '24491059':
        break
    tries += 1 
else:
    print("Wrong Password ")
    os._exit(0)
for i in range(len(username)):
    print(username[i] , '    :    ' , passwords[i])
command_help()
command = ""
while True:
    command = input()
    if command == 'N' or command == 'n':
        username1 = input("Enter the username ")
        passwords1 = input('Enter the password ')
        username.append(username1)
        passwords.append(passwords1)
        print("Added ")
    elif command == 'L' or command == 'l':
        for i in range(len(username)):
            print(i+1 , ".  ", username[i] , '\t' , passwords[i])
    elif command == "E" or command == 'e':
        for i in range(len(username)):
            print(i+1 , ".  ", username[i] , '\t' , passwords[i])
        index_selector = int(input("Enter the number of the term to be changed "))
        type_selector = input("To edit Password press p , for username press u ")
        index = index_selector - 1
        if type_selector == 'P' or type_selector == 'p':
            updated_value = input("Enter the changed pass ")
            passwords[index] = updated_value
            print("Value updated succesfully")
        elif type_selector == 'U' or type_selector == 'u':
            updated_value = input("Enter the changed username ")
            username[index] = updated_value
            print("Value updated succesfully")
    elif command.upper() == 'D':
        for i in range(len(username)):
            print(i+1 , ".  ", username[i] , '\t' , passwords[i])
        del_index = int(input("Enter the serial numnber of the username-password set you want to delete ")) - 1
        passwords.remove(passwords[del_index])    
        username.remove(username[del_index])
        print("Item removed successfully")
    elif command.upper() == 'S':
    	user_search = input("Enter the username / password you wish to search ")
    	if user_search in username:
    		index = username.index(user_search)
    		print(f"{username[index]}	{passwords[index]}")
    	elif user_search in passwords:
    		index = passwords.index(user_search)
    		print(f"{username[index]}	{passwords[index]}")
    elif command.upper() == "HELP":
        command_help()         
    elif command.upper() == 'Q':
    	os._exit(0)
    else:
        print("Invalid ")
