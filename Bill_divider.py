print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $\t"))
tip=int(input("How much tip would you like to give? 10, 12, or 15?\t"))
person=int(input("How many people to split the bill?\t"))
new_bill=((tip/100)*bill)+bill
pay_per_person=new_bill/person
print(f"Each person should pay: ${pay_per_person:.2f}")
