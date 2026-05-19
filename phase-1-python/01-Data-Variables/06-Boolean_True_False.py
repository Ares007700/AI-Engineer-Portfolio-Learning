status = input("is your account active? yes/no  ").lower()    #it directly converts input
if status in ["yes","y"]:
    account = True
else:
    account = False

if account:        #if will be executed only all form is true. true + true = true. true + flase = false
    print("Welcome")
else:
    print("Please fill up info and make your account active")

