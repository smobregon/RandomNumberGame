"""
Savannah Obregon
CS1213
02/12/16
Guessing Game
Random Number Practice 
"""
"""
import random
#randomly prints number between 1 and 6
a = random.randint(1,6)
print(a)
# randomly prints a number 10 times
for roll in range (10):
    a = random.randint(1,6)
    print(a)
"""

#Guessing Game program that picks a random number 
#allow user to guess what number was picked by the program
#user should keep guessing until he/she gets it correct
#program should display if users guess is lower or higher than the number picked
#keep count of how many guesses the user has entered until they get it right

import random

comp_num = random.randint(1,100)
count = 1

while True:
    
    user_num = int(input("Enter your guess: "))
    
    if int(user_num) == comp_num:
        print("Correct!")
        print("You have made", count,"attempts")
        break
    elif int(user_num < comp_num):
        print("Higher")
    else:
        print("Lower")
    count += 1







