Useful_Output = float(input("What was the total profit?  "))
Total_Input = float(input("How much did you invest?  "))
Efficiency = Useful_Output / Total_Input
print(f"The total efficiency in decimal is: {Efficiency:.2e}")  #.2f will extend 2 decimal number after calculation, 3 for 3 decimal
print(f"The total efficiency out of 100% is: {Efficiency:.1%}")  #.1% will show percentage as 1 decimal, 0 for no decimal

#: is format specifier .0f -> no decimal space. so the result will come as float but will show as int
#:, add comma as thousand seperator
#.2e scientific notation ^