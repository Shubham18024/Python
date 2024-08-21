ans = "y"
student_heights = []
while ans.lower() == "y":
    enter_heights = input("Enter the height of a student: ")
    try:
        student_heights.append(int(enter_heights))
    except ValueError:
        print("Please enter a valid number.")
    ans = input("Do you want to enter more? (y/n): ")
    if ans != "y":
        break

height = 0

number = 0
for i in student_heights:
    height += i
    number += 1

if number > 0:
    print(f"\ntotal height = {height}\nnumber of students = {number}\naverage height = {height/number:.0f}")
else:
    print("No valid heights entered.")
