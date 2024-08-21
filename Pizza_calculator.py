print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")  # Get pizza size
add_pepperoni = input("Do you want pepperoni? Y or N: ")    # Get pepperoni preference
extra_cheese = input("Do you want extra cheese? Y or N: ")  # Get extra cheese preference

# Initialize the bill
bill = 0

# Add base price based on size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid size selected.")
    exit()  # Exit if the size is invalid

# Add pepperoni cost
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Add extra cheese cost
if extra_cheese == "Y":
    bill += 1

# Print the final bill
print(f"Your final bill is: ${bill}.")




'''or , my answer
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0
if size == "S":
  bill+= 15
  if add_pepperoni == "Y":
    bill+=2
    if extra_cheese == "Y":
      bill+=1
      print(f"Your final bill is: ${bill}.")
    else:
      print(f"Your final bill is: ${bill}.")
  else :
    if extra_cheese == "Y":
      bill+=1
      print(f"Your final bill is: ${bill}.")
    else:
      print(f"Your final bill is: ${bill}.")

elif size == "M" or size == "L":
  
  if size == "M":
    bill+= 20
  elif size == "L":
    bill+=25
  
  if add_pepperoni == "Y":
    bill+=3
    if extra_cheese == "Y":
      bill+=1
      print(f"Your final bill is: ${bill}.")
    else:
      print(f"Your final bill is: ${bill}.")
  else :
    if extra_cheese == "Y":
      bill+=1
      print(f"Your final bill is: ${bill}.")
    else:
      print(f"Your final bill is: ${bill}.")
  
else:
  print("Wrong choice, please select between S,M and L")
  '''
