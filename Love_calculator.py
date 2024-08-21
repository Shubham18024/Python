print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") 
name2 = input("What is their name? ") 

# Write your code below this line 👇
a=0
b=0
list1=["t","r","u","e"]
list2=["l","o","v","e"]
name = name1+name2
for i in name.lower():
  if i in list1:
    a+=1
for j in name.lower():
  if j in list2:
    b+=1
score=int(str(a)+str(b))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")