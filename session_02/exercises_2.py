# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.
#width = 3
#length = 5
#area = width * length 
#print(area)

# 2. Write code that prints the length of the string, 'python'.
#name = "python"
#print(len(name))


# 3. Print out the first and third letter of the word 'python'.
#print(name[0],name[2])


# 4. Ask the user to enter their name, and print out `Hello, <name>`.
#name = input("What is your name?")
#print("hello "+name)

# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.
#age = int(input("What is your age?"))
#age_in_15_years = age + 15
#print("you will be "+ str(age_in_15_years))


# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.
#print("Hello, " + name + ", you are currently " + str(age) + " years old. In 15 years time you will be " + str(age_in_15_years))


# 7. Ask the user to enter their hometown, print it out in uppercase letters.
# hometown = input("What is your hometown?")
# print(hometown.upper())


# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.
# colour = input("what is your favourite colour?")
# print(len(colour))


# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.



# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.
# month = input("What is the month?")
# weather = input("what is the weather like today?")

# 11. Print out the above sentence but make the month upper case.

#print("it is " + month.upper() + " and it is " + weather + " today")

# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.
# favourite_animals = "My favourite animals:\n\tCats,\n\tDogs,\n\tWhales,\n\tHorses,\n\tLizards"

# print(favourite_animals)

# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.
# name = input("what is your name?\n")
# number = int(input("Pick a number:\n"))

# print(name[number].upper())

# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".
# print("welcometopython"[0:15:2])