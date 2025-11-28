line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️","⬜️","⬜️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Enter the coordinate in the form, A2,B3 etc : ") # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
cordinate_1 = int(position[1])-1
cordinate_2 = position[0]
if cordinate_2 == "A" :
  map[cordinate_1][0] = "X"
elif cordinate_2 == "B" :
  map[cordinate_1][1] = "X"
else :
  map[cordinate_1][2] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")