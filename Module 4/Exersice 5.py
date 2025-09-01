c_username ="python"
c_password ="rules"
tries = 0
while tries<5:
    username=input("Enter Username: ")
    password=input("Enter Password: ")
    if username == c_username and password == c_password:
        print("Welcome!")
        break
    else:
        print("Wrong username or password.Try again.")
        tries +=1
if tries==5:
    print("Access denied")


