print("Create your account")
username = input("Enter Username: ")
password = input("Enter Password: ")

print("Account created successfully")

print("Login now")
username1 = input("Enter Username: ")
password1 = input("Enter Password: ")
if username1 ==username and password1 == password:
    print("Logged In")
else:
    print("Invalid Login details, please try again")    
