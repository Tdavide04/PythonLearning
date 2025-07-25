#LEZIONE 3 - CICLI E CONDIZIONALI

#4-1. Pizzas: Think of at least three kinds of your favorite pizza. 
#Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. 
#For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
#Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
#The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, 
#such as I really love pizza!

list_pizza = ["capricciosa","rossa", "margherita"]
for pizza in list_pizza:
    print(pizza)
for pizza in list_pizza:
    print(f"This is my favorite pizza {pizza}")
print("I really like pizza")

# -> capricciosa
#rossa
#margherita
#This is my favorite pizza capricciosa
#This is my favorite pizza rossa
#This is my favorite pizza margherita
#I really like pizza

#4-2. Animals: Think of at least three different animals that have a common characteristic. 
#Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#Modify your program to print a statement about each animal, such as A dog would make a great pet.
#Add a line at the end of your program, stating what these animals have in common. 
#You could print a sentence, such as Any of these animals would make a great pet!

list_animals = ["dog", "cat", "fox"]
for animal in list_animals:
    print(animal)
for animal in list_animals:
    print(f"{animal} is a cute animal")
print("Any of these animals would make a great pet!")

# -> dog
#cat
#fox
#dog is a cute animal
#cat is a cute animal
#fox is a cute animal
#Any of these animals would make a great pet!

#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

for x in range(21):
    print(x)

# -> 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
#(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

my_list: list = [index for index in range(1000001)]
print(my_list)

# -> a list with numbers between 0 and 1000000

#4-5. Summing a Million: Make a list of the numbers from one to one million, 
#and then use min() and max() to make sure your list actually starts at one and ends at one million. 
#Also, use the sum() function to see how quickly Python can add a million numbers.

print(min(my_list)) 
print(max(my_list))
print(sum(my_list))

# -> 0
#1000000
#500000500000

#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
#Use a for loop to print each number.

for x in range(1, 21, 2):
    print(x)

# -> 1,3,5,7,9,11,13,14,15,17,19

#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

for x in range(3,33,3):
    print(x)

# -> 3,6,9,12,15,18,21,24,27,30

#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
#and use a for loop to print out the value of each cube.

for x in range(11):
    print(x**3)

# -> 0,1,8,27,64,125,216,343,512,729,1000

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cube_list: list = [index**3 for index in range(11)]
print(cube_list)

# -> [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

#4-10. Slices: Using one of the programs you wrote in this chapter, 
#add several lines to the end of the program that do the following:
#Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
#Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
#Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

print(f"The first three items in the list are: {cube_list[:3]}")
print(f"Three items from the middle of the list are: {cube_list[3:7]}")
print(f"The last three items in the list are: {cube_list[7:]}")

# -> The first three items in the list are: [0, 1, 8]
#Three items from the middle of the list are: [27, 64, 125, 216]
#The last three items in the list are: [343, 512, 729, 1000]

#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. 
#Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#Add a new pizza to the original list.
#Add a different pizza to the list friend_pizzas.
#Prove that you have two separate lists. Print the message My favorite pizzas are:, 
#and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, 
#and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

friend_pizzas = list_pizza
list_pizza.append("Quattro Stagioni")
friend_pizzas.append("Napoli")
for pizza in friend_pizzas:
    print(f"My friend’s favorite pizzas are: {pizza}")
for pizza in list_pizza:
    print(f"My favorite pizzas are: {pizza}")

# -> My friend’s favorite pizzas are: capricciosa
#My friend’s favorite pizzas are: rossa
#My friend’s favorite pizzas are: margherita
#My friend’s favorite pizzas are: Quattro Stagioni
#My friend’s favorite pizzas are: Napoli
#My favorite pizzas are: capricciosa
#My favorite pizzas are: rossa
#My favorite pizzas are: margherita
#My favorite pizzas are: Quattro Stagioni
#My favorite pizzas are: Napoli

#4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. 
#Choose a version of foods.py, and write two for loops to print each list of foods.

# -> done

#4-14. PEP 8: Look through the original PEP 8 style guide at https://python.org/dev/peps/pep-0008. 
#You won’t use much of it now, but it might be interesting to skim through it.

# -> done

#4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.

# -> done 

#5-1. Conditional Tests: Write a series of conditional tests. 
#Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
#Look closely at your results, and make sure you understand why each line evaluates to True or False.
#Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car == 'audi'? I predict False.")
print(car == 'audi')
print("Is car == 'ferrari'? I predict False.")
print(car == 'ferrari')
print("Is car != 'toyota'? I predict True.")
print(car != 'toyota')
print("Is car == 'volkswagen'? I predict False.")
print(car == 'volkswagen')
print("Is car == 'honda'? I predict False.")
print(car == 'honda')
print("Is car != 'tesla'? I predict True.")
print(car != 'tesla')
print("Is car != 'nissan'? I predict True.")
print(car != 'nissan')
print("Is car != 'bmw'? I predict True.")
print(car != 'bmw')

#Is car == 'subaru'? I predict True.
# True
# Is car == 'audi'? I predict False.
# False
# Is car == 'ferrari'? I predict False.
# False
# Is car != 'toyota'? I predict True.
# True
# Is car == 'volkswagen'? I predict False.
# False
# Is car == 'honda'? I predict False.
# False
# Is car != 'tesla'? I predict True.
# True
# Is car != 'nissan'? I predict True.
# True
# Is car != 'bmw'? I predict True.
# True

#5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10. 
#If you want to try more comparisons, write more tests and add them to conditional_tests.py. 
#Have at least one True and one False result for each of the following:
#Tests for equality and inequality with strings
#Tests using the lower() method
#Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, 
#and less than or equal to
#Tests using the and keyword and the or keyword
#Test whether an item is in a list
#Test whether an item is not in a list

'''
# Test for equality: 
'apple' == 'apple' (True)
# Test for inequality:
'apple' != 'orange' (True)
# Test for equality with lower(): 
'Apple'.lower() == 'apple' (True)
# Test for inequality with lower(): 
'OrAnge'.lower() != 'orange' (False)
# Numerical equality: 
5 == 5 (True)
# Numerical inequality: 
10 != 5 (True)
# Greater than: 
15 > 10 (True)
# Less than: 
20 < 30 (True)
# Greater than or equal to: 
25 >= 25 (True)
# Less than or equal to: 
30 <= 30 (True)
# Using and: 
(5 > 3) and (10 < 15) (True)
# Using or:
(5 < 3) or (10 == 10) (True)
if 'apple' is in ['apple', 'orange', 'banana'] (True)
if 'grape' is in ['apple', 'orange', 'banana'] (False)
if 'pear' is not in ['apple', 'orange', 'banana'] (True)
if 'orange' is not in ['apple', 'orange', 'banana'] (False)
'''

#5-3. Alien Colors #1: Imagine an alien was just shot down in a game. 
#Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
#Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
#Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

alien_color = "yellow"
if alien_color == "green":
    print("You earned 5 points")
else: 
    print("You lost")

alien_color = "green"
if alien_color == "green":
    print("You earned 5 points")


# -> You lost
#You earned 5 points

#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
#If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#Write one version of this program that runs the if block and another that runs the else block.

alien_color = "yellow"
if alien_color == "green":
    print("You earned 5 points")
elif alien_color == "yellow":
    print("You earned 10 points")
else:
    print("You lost")

# -> You earned 10 points

#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
#If the alien is green, print a message that the player earned 5 points.
#If the alien is yellow, print a message that the player earned 10 points.
#If the alien is red, print a message that the player earned 15 points.
#Write three versions of this program, making sure each message is printed for the appropriate color alien.

alien_color = "red"
if alien_color == "green":
    print("You earned 5 points")
elif alien_color == "yellow":
    print("You earned 10 points")
elif alien_color == "red":
    print("You earned 15 points")
else:
    print("You lost")

# -> You earned 15 points

#5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. 
#Set a value for the variable age, and then:
#If the person is less than 2 years old, print a message that the person is a baby.
#If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
#If the person is at least 4 years old but less than 13, print a message that the person is a kid.
#If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
#If the person is at least 20 years old but less than 65, print a message that the person is an adult.
#If the person is age 65 or older, print a message that the person is an elder.

age = 30
if age < 2:
    print("the person is a baby")
elif age >= 2 and age < 4:
    print("the person is a toddler")
elif age >= 4 and age < 13:
    print("the person is a kid")
elif age >= 13 and age < 20:
    print("the person is an teenager")
elif age >= 20 and age < 65:
    print("the person is a adult")
else:
    print("the person is elder")

# -> the person is an adult

#5-7. Favorite Fruit: Make a list of your favorite fruits, 
#and then write a series of independent if statements that check for certain fruits in your list.
#Make a list of your three favorite fruits and call it favorite_fruits.
#Write five if statements. Each should check whether a certain kind of fruit is in your list. 
#If the fruit is in your list, the if block should print a statement, such as You really like Apples!

favorite_fruits: list = ['apple', 'banana', 'orange']
if 'apple' in favorite_fruits:
    print("You really like Apples")
elif 'banana' in favorite_fruits:
    print("You really like Bananas")
elif 'orange' in favorite_fruits:
    print("You really like Oranges")
elif 'kiwi' in favorite_fruits:
    print("You really like Kiwis.")
elif 'strawberry' in favorite_fruits:
    print("You really like Strawberries.")

# -> You really like Apples!
# You really like Bananas!
# You really like Oranges!

#5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. 
#Imagine you are writing code that will print a greeting to each user after they log in to a website. 
#Loop through the list, and print a greeting to each user.
#If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
#Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.

usernames: list = ["admin", "davide", "simone", "alessia", "philip"]
if "admin" in usernames:
    print("Hello admin, would you like to see a status report?")
for x in usernames:
    if x is not "admin":
        print(f"Hello {x}, thank you for logging in again")

# -> Hello admin, would you like to see a status report?
# Hello davide, thank you for logging in again
# Hello simone, thank you for logging in again
# Hello alessia, thank you for logging in again
# Hello philip, thank you for logging in again

#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
#If the list is empty, print the message We need to find some users!
#Remove all of the usernames from your list, and make sure the correct message is printed.

usernames = []
if usernames == []:
    print("We need to find some users!")

# -> We need to find some users!

#5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#Make a list of five or more usernames called current_users.
#Make another list of five usernames called new_users. 
#Make sure one or two of the new usernames are also in the current_users list.
#Loop through the new_users list to see if each new username has already been used. 
#If it has, print a message that the person will need to enter a new username. 
#If a username has not been used, print a message saying that the username is available.
#Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
#(To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

current_users: list = ["davide", "simone", "alessia", "philip", "antonio"]
new_users: list = ["admin", "alessia", "DAVIDE", "bruce", "giovanni"]
for user in new_users:
    if user.lower() in current_users:
        print(f"the username {user} has already been used")
    else:
        print(f"the username {user} is available")

# -> the username admin is available
# the username alessia has already been used
# the username DAVIDE has already been used
# the username bruce is available
# the username giovanni is available

#5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. 
#Most ordinal numbers end in th, except 1, 2, and 3.
#Store the numbers 1 through 9 in a list.
#Loop through the list.
#Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. 
#Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

numbers: list = [index for index in range(1,10)]
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")

# -> 1st
# 2nd
# 3rd
# 4th
# 5th
# 6th
# 7th
# 8th
# 9th

