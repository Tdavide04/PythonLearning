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
'''
filename = "python_notes.txt"
filename1= filename.removesuffix(".txt")
print(filename1)
'''
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


