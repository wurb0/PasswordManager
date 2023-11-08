# password manager

# Input: add new password- gen new password; view all passwords

def view_pass():
    with open('passwords.txt', 'a') as file:
        
    return


def add_pass():
    username = input("Enter new username:\n")
    newpass = input("Enter new password:\n")

    with open('passwords.txt', 'a') as file:
        file.write(username+" "+newpass)

    return


def create_pass():
    return


main_pass = "123a"

if input("Enter main password\n"):
    flag = True
else:
    flag = False

while flag == True:  # view passwords #add password #create password
    case = input(
        "View all passwords, Add a new password or Create a new password (view,add,create)\n")
    if case == "view":
        view_pass()
    elif case == "add":
        add_pass()
    elif case == "create":
        create_pass
    else:
        print("Invalid Input, Try Again.\n")
