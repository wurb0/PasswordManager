# password manager
import os


def view_pass():
    if os.path.exists('passwords.txt'):
        with open('passwords.txt', 'r') as file:
            for line in file:
                username, password = line.split(" ")
                print("username: ", username, " password: ", password, "\n")
    else:
        print("Passwords.txt file not found")
    return


def add_pass():
    username = input("Enter new username:\n")
    newpass = input("Enter new password:\n")

    with open('passwords.txt', 'a') as file:
        file.write(username+" "+newpass + "\n")

    return


def create_pass():

    return


def search(findusername):
    with open('passwords.txt', 'r') as file:
        for line in file:
            username, password = line.split(" ")
            if username == findusername:
                print(password)


main_pass = "a"

if input("Enter main password\n"):
    flag = True
else:
    flag = False

while flag == True:  # view passwords #add password #create password

    case = input(
        "View all passwords, Add a new password, Create a new password or Search for a password(view,add,create,search and q to quit)\n")
    if case == "view":
        view_pass()
    elif case == "add":
        add_pass()
    elif case == "create":
        create_pass
    elif case == "search":
        username = input("Enter a username to view its password\n")
        search(username)
    elif case == "q":
        flag = False
        break
    else:
        print("Invalid Input, Try Again.\n")
