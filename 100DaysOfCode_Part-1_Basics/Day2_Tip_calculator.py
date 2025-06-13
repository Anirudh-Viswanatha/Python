print("Welcome to the Tip Calculator.")
bill=float(input("What was the total bill? "))
Tip=float(input("What percentage tip would you like to give? 10%, 12%, or 15%? "))
people=int(input("How many people to split the bill? "))
tip=bill*(Tip/100)
total_bill_per_person = (bill + tip)/people
# bill_per_person=round(total_bill_per_person,2) --> This sometimes gives only one decimal if 2nd decimal value is 0, its not shown. To fix this type of issues, we can use "{:.2f}".format(<number>) as mentioned below. This "{:.2f}".format(<number>) converts a float <number> into string
bill_per_person="{:.2f}".format(total_bill_per_person)
print(f"Each person should pay: ${bill_per_person}")
