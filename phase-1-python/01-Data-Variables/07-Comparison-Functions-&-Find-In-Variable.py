cat = input("Name of your cat?  ").strip().lower()
if cat == "piku":   #meaning == is "piku" inside cat variable
    print ("It's your cat")
else:
    print ("It's not your cat")


#== asks are this two equal 5==5 True , 5==6 False
#!= asks are this two not equal 5!=5 False ,  5!=6 True
#> asks if left side is bigger 5>9 True , 7>8 False
#< asks if left side is smaller 4<7 True , 8<3 False
#>= bigger then or equal to 5>=5 True , 6>=5 True , 2>=5 False
#<= less then or equal to 6<=6 True , 6<=8 True, 6<=3 False
#always write comparism after if, or it will be ignored