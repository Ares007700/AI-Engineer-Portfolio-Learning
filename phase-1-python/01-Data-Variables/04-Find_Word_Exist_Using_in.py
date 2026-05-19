Complaint = input("Please provide feedback  ")
if 'bad' in Complaint.lower():        #in -> searches 'bad' in the complaint input given. 
    print ("Thanks for your feedback. We will try to improve.")
else :
    print ("Thanks for supporting. Stay with us")  #tab space must be given while using if/ elif/ else statement

#for .lower()  all input will be converted in lower case to search 'bad' 
#if .lower() is not given BAD will not match with 'bad'  so output will be from else 
#need to always convert so that i won't have to type all forms of 'bad'