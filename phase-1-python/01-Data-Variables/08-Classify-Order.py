Order_Amount = input("Please enter your order ammount  ")
Order_Amount = float(Order_Amount)
if Order_Amount < 1000 :
    print ("Small Order")
elif Order_Amount <= 5000 :   #this will cover 1000 to 5000 inclusive 
    print ("Medium Order")
else :                        #it will be auto,    > 5000 
    print ("Large Order")

# altnative - Order_Amount >1000 or Order_Amount < 5001