#LEZIONE 2 - TIPI DI DATO, OPERAZAZIONI, COLLECTION

#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. 
# Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

# -> Hello Eric, would you like to learn some Python today?

#2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

name = "Eric"
print(name.lower())
print(name.upper())
print(name.title())

# -> eric
# ERIC
# Eric

# 2-5/6. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
# Your output should look something like the following, including the quotation marks: 
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”

famous_person = "George Bernard Shaw"
famous_quote = "Se tu hai una mela, e io ho una mela, e ce le scambiamo, allora tu ed io abbiamo sempre una mela ciascuno. Ma se tu hai un'idea, ed io ho un'idea, e ce le scambiamo, allora abbiamo entrambi due idee."

print(f"{famous_person} once said, \"{famous_quote}\"")

# -> George Bernard Shaw once said, "Se tu hai una mela, e io ho una mela, e ce le scambiamo, 
# allora tu ed io abbiamo sempre una mela ciascuno. Ma se tu hai un'idea, ed io ho un'idea, e ce le scambiamo, 
# allora abbiamo entrambi due idee."

#2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
#Assign the value 'python_notes.txt' to a variable called filename. 
#Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

filename = "python_notes.txt"
filename1= filename.removesuffix(".txt")
print(filename1)

# -> "python_notes"
#3-1. Names: Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.

names = ["Alessia", "Simone", "Antonio", "Philip"]
for name in names:
    print(name)

# -> Alessia
# Simone
# Antonio
# Philip

 #3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
 # The text of each message should be the same, but each message should be personalized with the person’s name.
 
for name in names:
    print(f"Hello {name} how are you?")
    
# -> Hello Alessia how are you?
#Hello Simone how are you?
#Hello Antonio how are you?
#Hello Philip how are you?

#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
# Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

cars = ["Ferrari", "Lamborghini", "Porsche", "Mercedes", "BMW"]
for car in cars:
    print(f"I would like to own a {car}")
    
# -> I would like to own a Ferrari
#I would like to own a Lamborghini
#I would like to own a Porsche
#I would like to own a Mercedes
#I would like to own a BMW

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.

for name in names:
    print(f"Hey {name}, this is the invitation to come to dinner with me")
    
# -> Hey Alessia, this is the invitation to come to dinner with me
# Hey Simone, this is the invitation to come to dinner with me
# Hey Antonio, this is the invitation to come to dinner with me
# Hey Philip, this is the invitation to come to dinner with me

#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

names[3] = "Robert"
for name in names:
    print(f"Hey {name}, unfortunatly Philip can't be with us, so this is the new invitation to come to dinner with me")
    
# -> Hey Alessia, unfortunatly Philip can't be with us, so this is the new invitation to come to dinner with me
# Hey Simone, unfortunatly Philip can't be with us, so this is the new invitation to come to dinner with me
# Hey Antonio, unfortunatly Philip can't be with us, so this is the new invitation to come to dinner with me
# Hey Robert, unfortunatly Philip can't be with us, so this is the new invitation to come to dinner with me

#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

names.insert(0, "Giovanni")
names.insert(2, "Francesca")
names.append("Luca")
print("I found a bigger table")
for name in names:
    print(f"Hi {name}, since i found a bigger table i send this invitation for the new and old people as a conferm")


# -> I found a bigger table
#Hi Giovanni, since i found a bigger table i send this invitation for the new and old people as a conferm
#Hi Alessia, since i found a bigger table i send this invitation for the new and old people as a conferm
#Hi Francesca, since i found a bigger table i send this invitation for the new and old people as a conferm
#Hi Simone, since i found a bigger table i send this invitation for the new and old people as a conferm
#Hi Antonio, since i found a bigger table i send this invitation for the new and old people as a conferm
#Hi Robert, since i found a bigger table i send this invitation for the new and old people as a conferm
#Hi Luca, since i found a bigger table i send this invitation for the new and old people as a conferm

#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, 
# print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

while len(names)>2:
    names1 = names.pop()
    print(f"Sorry {names1} i dont have enough space for you")
for name in names:
    print(f"{name} you are still invited")
del names[:]
print(names)

# -> Sorry Luca i dont have enough space for you
# Sorry Robert i dont have enough space for you
# Sorry Antonio i dont have enough space for you
# Sorry Simone i dont have enough space for you
# Sorry Francesca i dont have enough space for you
# Giovanni you are still invited
# Alessia you are still invited

#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse()  to change the order of your list. Print the list to show that its order has changed.
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.

places = ["Sweden", "France", "Iceland", "Portugal", "Germany"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse = True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

# -> ['Sweden', 'France', 'Iceland', 'Portugal', 'Germany']
# ['France', 'Germany', 'Iceland', 'Portugal', 'Sweden']
# ['Sweden', 'France', 'Iceland', 'Portugal', 'Germany']
# ['Sweden', 'Portugal', 'Iceland', 'Germany', 'France']
# ['Sweden', 'France', 'Iceland', 'Portugal', 'Germany']
# ['Germany', 'Portugal', 'Iceland', 'France', 'Sweden']
# ['Sweden', 'France', 'Iceland', 'Portugal', 'Germany']
# ['France', 'Germany', 'Iceland', 'Portugal', 'Sweden']
# ['Sweden', 'Portugal', 'Iceland', 'Germany', 'France']

#3-9. Dinner Guests: Working with one of the programs from Exercises 3, 
# use len() to print a message indicating the number of people you’re inviting to dinner.

print(len(names1))

# -> 9

#3-10. Every Function: Think of things you could store in a list. 
# For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

list = []
list.insert(0, "Giovanni")
list.append("Luca")
list.sort()
list.reverse()
list.pop()
del list[:]
print(list)

# -> []

#6-1. Person: Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

dict = {"first_name":"Philip", "last_name":"Vicari", "age":19, "city":"Milano"}
print(dict)

# -> {'first_name': 'Philip', 'last_name': 'Vicari', 'age': 19, 'city': 'Milano'}

#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. 
# Think of a favorite number for each person, and store each as a value in your dictionary. 
# Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

dict1={"Philip":90, "Davide":17, "Simone": 19, "Alessia": 25, "Francesca": 9}
print(dict1)

# -> {'Philip': 90, 'Davide': 17, 'Simone': 19, 'Alessia': 25, 'Francesca': 9}

#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. 
# You might print the word followed by a colon and then its meaning, 
# or print the word on one line and then print its meaning indented on a second line. 
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {"for":"The for loop is used to iterate over a sequence",
            "while":"The while loop is used to execute a block of code repeatedly as long as a specified condition is true",
            "sort()":"The sort() method is used to sort elements in a list in ascending order.",
            "reverse()":"The reverse() method is used to reverse the order of elements in a list",
            "pop()":"The pop() method is used to remove and return an element from a specific index in a list"}

#6-7. People: Start with the program you wrote for Exercise 6-1. 
# Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
# Loop through your list of people. As you loop through the list, print everything you know about each person.

people = [{"first_name":"Philip", "last_name":"Vicari", "age":19, "city":"Milano"},
          {"first_name":"Davide", "last_name":"Trischitta", "age":20, "city":"Roma"},
          {"first_name":"Alessia", "last_name":"Agosti", "age":17, "city":"Roma"}]

for person in people:
    print("First Name:", person["first_name"])
    print("Last Name:", person["last_name"])
    print("Age:", person["age"])
    print("City:", person["city"])
    
# -> First Name: Philip
# Last Name: Vicari
# Age: 19
# City: Milano
# First Name: Davide
# Last Name: Trischitta
# Age: 20
# City: Roma
# First Name: Alessia
# Last Name: Agosti
# Age: 17
# City: Roma

#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. 
# Next, loop through your list and as you do, print everything you know about each pet. 

pet1 = {"animal": "Dog", "owner": "Alice"}
pet2 = {"animal": "Cat", "owner": "Bob"}
pet3 = {"animal": "Bird", "owner": "Charlie"}
pets = [pet1, pet2, pet3]

for pet in pets:
    print("Pet Type:", pet["animal"])
    print("Owner:", pet["owner"])

# -> Pet Type: Dog
# Owner: Alice
# Pet Type: Cat
# Owner: Bob
# Pet Type: Bird
# Owner: Charlie

#6-9. Favorite Places: Make a dictionary called favorite_places. 
# Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
# To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
# Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places = {"Alessia":"Sweden", "Philip":"Poland", "Davide":"Germany"}
for keys, values in favorite_places.items():
    print(keys, values)
    
# -> Alessia Sweden
# Philip Poland
# Davide Germany

#6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.

dict1={"Philip":"90, 18, 447874373", "Davide":"17, 7, 98", "Simone": "19, 843, 98", "Alessia": "25, 65, 87, 23", "Francesca": "9, 8, 5"}
for keys, values in dict1.items():
    print(keys, values)
    
# -> Philip 90, 18, 447874373
# Davide 17, 7, 98
# Simone 19, 843, 98
# Alessia 25, 65, 87, 23
# Francesca 9, 8, 5

#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, 
# its approximate population, and one fact about that city. 
# The keys for each city’s dictionary should be something like country, population, and fact. 
# Print the name of each city and all of the information you have stored about it.

cities = {
    "Tokyo": {
        "country": "Japan",
        "population": "9.7 million",
        "fact": "Tokyo is the largest metropolitan area in the world."
    },
    "London": {
        "country": "United Kingdom",
        "population": "8.9 million",
        "fact": "London has a history dating back over 2,000 years."
    },
    "New York City": {
        "country": "United States",
        "population": "8.4 million",
        "fact": "New York City is known as the city that never sleeps."
    }
}

for keys, values in cities.items():
    print(f"City: {keys}")
    print(f"Country: {values['country']}")
    print(f"Population: {values['population']}")
    print(f"Fact: {values['fact']}")

# -> City: Tokyo
# Country: Japan
# Population: 9.7 million
# Fact: Tokyo is the largest metropolitan area in the world.
# City: London
# Country: United Kingdom
# Population: 8.9 million
# Fact: London has a history dating back over 2,000 years.
# City: New York City
# Country: United States
# Population: 8.4 million
# Fact: New York City is known as the city that never sleeps.

#6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. 
# Use one of the example programs from this chapter, and extend it by adding new keys and values, 
# changing the context of the program, or improving the formatting of the output.

#6-1 = changed
dict = [{"first_name":"Philip", "last_name":"Vicari", "age":19, "city":"Napoli"},
{"first_name":"Davide", "last_name":"Trischitta", "age":20, "city":"Roma"}]

