# password manager
import os
import secrets
import string


def view_pass():
    if os.path.exists('passwords.txt'):
        with open('passwords.txt', 'r') as file:
            for line in file:
                username, password = line.split(" ")
                print("username: ", username, " password: ", password, "\n")
    else:
        print("Passwords.txt file not found, add a new password first")
    return


def add_pass(username, newpass):

    with open('passwords.txt', 'a') as file:
        file.write(username+" "+newpass + "\n")

    return


def create_pass(length):
    exclude = "\n |`~   "
    flag = input(
        "Are there any characters/symbols to exclude from the generated password? y/n: \n")
    if (flag == "y"):
        exclude = input(
            "Enter characters to exclude from the generated password without separation:\n")
        exclude = exclude.strip()
        chars = ''.join(
            char for char in string.printable if char not in exclude)
        genpass = ''.join(secrets.choice(chars)for char in range(length))
        print(genpass)
    elif (flag == "n"):
        chars = ''.join(
            char for char in string.printable if char not in exclude)
        genpass = ''.join(secrets.choice(chars)for char in range(length))
        print(genpass)

    # add new password to file
    if input("Would you like to add this new password? (y/n)\n") == "y":
        username = input("Enter username:\n")
        add_pass(username, genpass)

    return


def search(findusername):
    with open('passwords.txt', 'r') as file:
        for line in file:
            username, password = line.split(" ")
            if username == findusername:
                print(password)


main_pass = "a"

if input("Enter main password\n") == main_pass:
    flag = True
else:
    flag = False

while flag == True:  # view passwords #add password #create password

    case = input(
        "View all passwords, Add a new password, Create a new password or Search for a password (view,add,create,search and q to quit)\n")
    if case == "view":
        view_pass()
    elif case == "add":
        username = input("Enter new username:\n")
        newpass = input("Enter new password:\n")
        add_pass(username, newpass)
    elif case == "create":
        length = int(input("How long should the password be?\n"))
        create_pass(length)
    elif case == "search":
        username = input("Enter a username to view its password\n")
        search(username)
    elif case == "q":
        flag = False
        break
    else:
        print("Invalid Input, Try Again.\n")
