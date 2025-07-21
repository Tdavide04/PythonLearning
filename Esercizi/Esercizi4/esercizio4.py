#LEZIONE 4 - PROBLEM SOLVING, ERRORI E FUNZIONI

#8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. 
#Call the function, and make sure the message displays correctly.

def display_message():
    print("I'am learning python stuff")

display_message()

# -> I'am learning python stuff

#8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
#The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
#Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(title):
    print("One of my favorite books is Alice in Wonderland")

title = "Alice in Wonderland"
favorite_book(title)

# -> "One of my favorite books is Alice in Wonderland"

#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
#The function should print a sentence summarizing the size of the shirt and the message printed on it. 
#Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, text):
    print(f"the size of your shirt is {size}, while your text message is \"{text}\"")

make_shirt("Large", "Forza Napoli")
make_shirt(size = "Medium", text = "Hello world!")

# -> the size of your shirt is Large, while your text message is "Forza Napoli"
#the size of your shirt is Medium, while your text message is "Hello world!"

#8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size='large', message='I love Python'):
    print(f"Creating a {size} shirt with the message: {message}")
make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='Hello World!')

# -> Creating a large shirt with the message: I love Python
#Creating a medium shirt with the message: I love Python
#Creating a small shirt with the message: Hello World!

#8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
#The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. 
#Call your function for three different cities, at least one of which is not in the default country.

def describe_city(name, country):
    print(f"{name} is in {country}")
describe_city("Paris", "France")
describe_city("Rome", "Italy")
describe_city("Valencia", "Spain")

# -> Paris is in France
#Rome is in Italy
#Valencia is in Spain

#8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
#The function should return a string formatted like this: "Santiago, Chile". 
#Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(name, country):
    print(f"{name}, {country}")
city_country("Paris", "France")
city_country("Rome", "Italy")
city_country("Valencia", "Spain")

# -> Paris, France
#Rome, Italy
#Valencia, Spain

#8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
#The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
#Use the function to make three dictionaries representing different albums. 
#Print each return value to show that the  dictionaries are storing the album information correctly. 
#Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
#If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
#Make at least one new function call that includes the number of songs on an album.

def make_album(artist_name, album_title):
    album_dict = {
        "artist": artist_name.title(),
        "title": album_title.title()
    }
    print(f"here there are your album {album_dict}")
    return album_dict

album = make_album("Queen", "Queen")
album = make_album("Kanye West", "Ye")
album = make_album("Taylor Swift", "Lover")

# -> here there are your album {'artist': 'Queen', 'title': 'Queen'}
#here there are your album {'artist': 'Kanye West', 'title': 'Ye'}
#here there are your album {'artist': 'Taylor Swift', 'title': 'Lover'}

#8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. 
#Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
'''
while True:
    if True:
        artist_name = input("Enter the artist's name: ")
        album_title = input("Enter the album title: ")
        make_album(artist_name, album_title)
    else:
        break
'''
#8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.def 

list1 = [
    "Hello!",
    "How are you?",
    "What's up?",
    "Good morning!"
    ]

def show_messages(list1: list):
    print("showing messages: ")
    for e in list1:
        print(e)

show_messages(list1)

# -> showing messages:
# Hello!
# How are you?
# What's up?
# Good morning!

#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
#Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
#After calling the function, print both of your lists to make sure the messages were moved correctly.
        
def send_messages(list1):
    print("sending messages: ")
    sent_messages = []
    while list1:
        current_message = list1.pop()
        print(current_message)
        sent_messages.append(current_message)
    return sent_messages   
send_messages(list1)
print(list1)

# -> sending messages:
# Hello!
# How are you?
# What's up?
# Good morning!
# []

#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
#After calling the function, print both of your lists to show that the original list has retained its messages.
        
def send_messages(list1):
    print("sending messages: ")
    sent_messages = []
    while list1:
        current_message = list1.pop()
        print(current_message)
        sent_messages.append(current_message)
    return sent_messages   
send_messages(list1)
print(list1)

# -> non ho capito la consegna

#8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
#The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. 
#Call the function three times, using a different number of arguments each time.

def make_sandwich(*ingredients):
    print(f"Making a sandwich with the following ingredients: {ingredients}")
    
make_sandwich('lettuce', 'tomato', 'cheese')
make_sandwich('turkey', 'bacon', 'avocado', 'mayonnaise')
make_sandwich('ham', 'swiss cheese', 'mustard', 'pickles', 'onions')

# -> Making a sandwich with the following ingredients: ('lettuce', 'tomato', 'cheese')
# Making a sandwich with the following ingredients: ('turkey', 'bacon', 'avocado', 'mayonnaise')
# Making a sandwich with the following ingredients: ('ham', 'swiss cheese', 'mustard', 'pickles', 'onions')

#8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. 
#All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"

def build_profile(fisrt_name, last_name, age, hair_color, weight):
    profile = {"first name" : fisrt_name,
               "last name" : last_name,
               "age" : age,
               "hair color" : hair_color,
               "weight" : weight
               }
    
    print(f"your profile is: {profile}")
    return profile

build_profile("davide", "trischitta", 20, "brown", 79)

# -> your profile is: {'first name': 'davide', 'last name': 'trischitta', 'age': 20, 'hair color': 'brown', 'weight': 79}

#8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. 
#It should then accept an arbitrary number of keyword arguments. 
#Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
#Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) 
#Print the dictionary that’s returned to make sure all the information was stored correctly. 

def make_car(manufacturer, model, color, seats):
    profile = {"manufacturer" : manufacturer,
               "model" : model,
               "color" : color,
               "seats" : seats
               }
    
    print(f"your car's profile is: {profile}")
    return profile

car = make_car('subaru', 'outback', color='blue', seats = 4)

# -> your car's profile is: {'manufacturer': 'subaru', 'model': 'outback', 'color': 'blue', 'seats': 4}

#8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
#Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
'''
import printing_functions
printing_functions.printing("audi", "sedans", color = "red", seats = 2)

#non ho capito perche non funziona
'''

#8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. 
#Import the function into your main program file, and call the function using each of these approaches:
'''
import printing_functions
from printing_functions import printing
from printing_functions import printing as fn
import printing_functions as mn
from printing_functions import *
'''
#8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.
