x = input("How much ammount did you spend?  ")                #this takes data as input text and = makes the variable 
price = float(x)                                             #convert x by int or float for making that string to number, in this case I have given float so that even cent would be counted as decimal form
if price > 500:                                              #if/ else/ elif conditions
    print ("Congratulations! You have got 10% discount!")
elif price > 200:
    print ("You are almost there to get a discount.")
else: 
    print ("Sorry, no discount in this ammount.")


    # Variables store data
#name = 'Aryan'          # str  — text (string)
#age = 22                # int  — whole number (integer)
#gpa = 3.87              # float — decimal number
#is_student = True       # bool — True or False
 
# Use print() to see the value stored inside
#print(name)             # Output: Aryan
#print(age)              # Output: 22
#print(type(age))        # Output: <class 'int'>
#always write comparism after if, or it will be ignored