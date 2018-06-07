import random

name = input("Enter your name: ")

age = int(input ("Enter  a number between 1 to 9"))

number = random.randint (1,9)

if age < number:

   print("Number you gusessed is less than generated one")

elif age > number:
   print("Number you guessed is more than generated one")


else:
   print("You guessed just right")




print ("Your name is %s, Your age is %d"  %(name, age))