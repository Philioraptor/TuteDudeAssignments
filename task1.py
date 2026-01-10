#Task 1: Check if a Number is Even or Odd


x = int(input("Enter the Number:"))

#checking the number is even or odd
if(x%2==0):
  print(f"The Entered number {x} is even. ")
elif(x%2!=0):
  print(f"The Entered number {x} is odd. ")
else:
  print("Invalid Input. Please try again")
