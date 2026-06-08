confidence = float(input("Provide Confidence Level  "))
feedback = input("Please share your thoughts  ").lower()

bad_keyword = ["complaint","bad","manager","refund","policy"]

if confidence >= 0.85 and not any (word in feedback for word in bad_keyword) : 
    print ("auto reply")
else :
    print ("human review")           


#(word in feedback for word in bad_keyword)  is a generator expression that checks each word in bad_keyword to see if it exists in feedback