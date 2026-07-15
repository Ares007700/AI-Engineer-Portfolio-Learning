from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 
#this will create a CryptContext object that uses bcrypt for hashing passwords

hashed = pwd_context.hash("mypassword") #this will hash the password "mypassword" using bcrypt
print("Hashed:", hashed)  #this will print the hashed password, something like $2b$12$Kx....
print("Verify correct:", pwd_context.verify("mypassword", hashed)) #this will return True since the password is correct
print("Verify wrong:", pwd_context.verify("wrongpass", hashed)) #this will return False since the password is incorrect