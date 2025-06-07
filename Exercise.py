# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 01:54:24 2023

@author: Sunil
"""

# =============================================================================
# # Exercise-1
# Name = 'John Smith'
# Age = 20
# Is_the_patient_new = True
# print(Name,Age,Is_the_patient_new)
# =============================================================================

# =============================================================================
# # Exercise 2
# Name = input('What is your name? ')
# Favourite_Colour = input('What is your favourite colour? ')
# print(Name+' likes '+Favourite_Colour)
# =============================================================================

# Exercise 3
# Your_Weight = input('What is your weight? ')
# Weight = (float(Your_Weight)*0.4535 )
# print('weight(In Kilograms) = '+str(Weight))


# =============================================================================
# # Exercise 4
# Name = 'Sunil Kumar Panda'
# print(Name.find('a'))
# print(Name.title())
# print(len(Name))
# print('sunil' in Name)
# =============================================================================

# =============================================================================
# # Exercise 5
# X = -17/3
# print(X)
# print(abs(X))
# print(abs(round(X)))
# =============================================================================

# =============================================================================
# # Exercise 6
# 
# Temp = input("What is today's temperature? ")
# 
# if int(Temp) > 40:
#     is_hot = True
#     print("It's a hot day.")
# elif int(Temp) < 20:
#     is_cold = True
#     print("It's a cold day.")
# else:
#     is_normal_day = True
#     print("It's a lovely day.")
# print("Enjoy your day.")
# 
# =============================================================================

# =============================================================================
# # Exercise 7
# 
# Name = input('Please type your name? ')
# if len(Name) <= 3:
#     print("Name must be at least 3 characters long.")
# elif len(Name) >= 10:
#     print("Name must be less than 50 characters long.")
# else:
#     print("Name looks good.")
# =============================================================================
    
# =============================================================================
# # Exercise 8
# Weight = int(input("What is your weight? "))
# UoM = input("What is your weight UoM? ")
# 
# if UoM.upper() == 'L':
#     weight = int(Weight*0.453592)
#     print(f'''Hi,
# Your weight is {weight}kgs.
# Thank you for your co-operation.''')
# elif UoM.upper() == 'K':
#      weight = int(Weight/0.453592)
#      print(f'''Hi,
#  Your weight is {weight}pounds.
#  Thank you for your co-operation.''')
# else:
#     print("Please selct UoM of weight measurement.")
# =============================================================================

# =============================================================================
# # Exercise 9
# 
# Secret_number = 9
# guess_count = 0 
# guess_limit = 3
# 
# while guess_count<guess_limit:
#     guess = int(input('Guess: '))
#     guess_count+=1
#     if guess == Secret_number:
#         print('You won.')
#         break
# else:
#      print('You failed.')
# =============================================================================

# =============================================================================
# # Exercise 10 - Car game
# Initial_Screen = input("> ")
# 
# if Initial_Screen.lower() == 'help':
#     print('Start - To start the car')
#     print('Stop - To stop the car')
#     print('Quit - To exit the game')
# elif Initial_Screen.lower() == 'start':
#     print('car started...Ready to GO.')
# elif Initial_Screen.lower() == 'stop':
#     print('car stopped')
# elif Initial_Screen.lower() == 'quit':
#     exit()
# else:
#     print("i don't understand that.")
# =============================================================================

# =============================================================================
# # Exercise 11
# command = ""
# car_started = False
# while True:
#     command = input("> ").lower()
#     if command=="start":
#         if car_started:
#             print("car already started...Let's Go")
#         else:
#             car_started = True
#             print("car started...Let's Go.")
#     elif command == 'stop':
#         if not car_started:
#             print("car already stopped")
#         else:
#             car_started = False
#             print("car stopped.")
#     elif command == 'help':
#         print("""
# Start - To start the car.
# Stop - To stop the car.
# Quit - To exit the game.
#               """)
#     elif command == 'quit':
#         break
#     else:
#         print("I don't understand this")
# =============================================================================

# =============================================================================
# # Exercise 12
# 
# Prices = [10,20,30]
# Total = 0
# for price in Prices:
#     Total += price
#     print(Total)
# =============================================================================

# =============================================================================
# # Exercise 13
# 
# numbers = (5,2,5,2,2) 
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'X'
#         print(output)
# =============================================================================

# Self Exercise 14

Numbers = [3,6,2,8,4,10]
Max = Numbers[0]
for number in Numbers:
    if number > Max:
        Max = number
        print(Max )



























