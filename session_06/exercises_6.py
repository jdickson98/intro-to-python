# Session 6 Exercises

## Section A
# 1. Create the following dictionary for an apple: Type = "Bramley", Price = 0.39, Colour = "Green".

# apple = {
#     "Type": "Bramley",
#     "Price": 0.39,
#     "Colour": "Green"
# }

# print(apple)

# 2. Add the best before date to the dictionary - print the dictionary.

# apple["best before date"] = "08/10/2023",

# print(apple)


# 3. Change the price to 0.41 - print the dictionary.

# apple["Price"] = 0.41,

# print(apple)

# 4. Set the apple to be on offer using a Boolean - print the dictionary.

# apple["Offer"] = True,

# print(apple)

# 5. The offer has now expired, remove the key/value from the dictionary - print the dictionary.

# del(apple["Offer"])

# print(apple)

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask the user to enter a persons name, if they enter a name, ask for the persons age. Store this information in a dictionary inside a list. 
#   Continue to ask for names until no name is given. Then print out all of the names and ages collected.

# people = []
# fname = None

# while fname != "":
#     fname = input("What is your first name? ")
#     if fname:
#         age = int(input("What is your age? "))
#         people.append(
#             {
#                 "fname": fname,
#                 "age": age
#             }
#         )
# print(people)

# 2. Create a restaurants menu with 5 items. Store this information in a dictionary inside a list. 
#   Each item in the menu should have the name of the item, the price and if it's vegetarian friendly (make at least one vegetarian friendly dish). 
#   Print out the entire menu. Print out the name of the vegetarian option(s).

# menu = [
#   {"food": "steak", "price": "$23", "veggie": False},
#   {"food": "ceasar salad", "price": "$15", "veggie": False},
#   {"food": "fries", "price": "$4", "veggie": True},
#   {"food": "carbonara", "price": "$14", "veggie": False},
#   {"food": "tomatoes", "price": "$2", "veggie": True}
# ]

# for item in menu:
#   if item["veggie"]:
#     print(item["food"])
    
# 3. The beetle game is a dice game where depending on what you roll is how much of the beetle you can draw.
#   If you roll a 6, you can draw the body
#   If you roll a 5, you can draw the head
#   If you roll a 4, you can draw the legs (but remember, you cannot draw legs without a body)
#   If you roll a 3, you can draw the antenna (but remember, you cannot draw antenna without a head)
#   If you roll a 2, you can draw the eyes (but remember, you cannot draw eyes without a head)
#   If you roll a 1, you can draw the mouth (but remember, you cannot draw a mouth without a head)
#   You need 6 legs, 2 antenna, 2 eyes, 1 mouth.
#   The player to complete the beetle in the fewest rolls of the dice wins. Create the beetle game.

# import random
# parts = {
#     "1": "Eye",
#     "2": "Mouth",
#     "3": "Antennae",
#     "4": "Leg",
#     "5": "Head",
#     "6": "Body"
# }
# beetles = []
# scores = []

# players = int(input("Please enter the number of players: "))

# for x in range(players):
#     beetles.append({
#         "1": 2,  # eyes
#         "2": 1,  # mouth
#         "3": 2,  # antennae
#         "4": 6,  # legs
#         "5": 1,  # head
#         "6": 1  # body
#     })
#     scores.append(0)

# print("LETS START!!!!!")
# winner = None

# while not winner:
#     for current_player in range(players):

#         x = input("Player " + str(current_player) + ": Roll the dice...")
#         if x == "q":
#             break
#         dice_roll = str(random.randint(1, 6))
#         scores[current_player] += 1
#         print("You rolled a: " + dice_roll)
#         if beetles[current_player][dice_roll] > 0:
#             if dice_roll == "1" and beetles[current_player]["5"]:
#                 print("Can't have an eye without a head")
#             elif dice_roll == "2" and beetles[current_player]["5"]:
#                 print("Can't have a mouth without a head")
#             elif dice_roll == "3" and beetles[current_player]["5"]:
#                 print("Can't have an antenna without a head")
#             elif dice_roll == "4" and beetles[current_player]["6"]:
#                 print("Can't have a leg without a body")
#             else:
#                 # valid roll therefore remove it from required go's
#                 print("You got a " + parts[dice_roll])
#                 beetles[current_player][dice_roll] -= 1
#                 for body_part in beetles[current_player]:
#                     if beetles[current_player][body_part]:
#                         print("You need " +
#                               str(beetles[current_player][body_part]) + " " + parts[body_part])
#                 if sum(beetles[current_player].values()) == 0:
#                     winner = current_player

# print("The winner is: " + str(winner))

# print(scores)
