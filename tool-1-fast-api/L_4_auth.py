from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 
#this will create a CryptContext object that uses bcrypt for hashing passwords

hashed = pwd_context.hash("hello123")   #this will hash the password "hello123" using bcrypt    
print(hashed)  # something like $2b$12$Kx....

is_correct = pwd_context.verify("hello123", hashed)  #it verifies the password against the hash 
print(is_correct)  # True