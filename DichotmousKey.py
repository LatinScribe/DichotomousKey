"""Dichotomous key program"""
import os
import sys

# constant options
YES = "1"
NO = "2"
START_OVER = "3"
PREV = "4"
EXIT = "5"

# --------- Defining all the custom functions ---------

# first option
def seeds():
# clear the screen
os.system('cls')
print("Fruits and Vegetables Dichotomous Key")
seeds = input("Does it have seeds?\n1. yes 2. no: ")
if seeds == YES:
    red()
elif seeds == NO:
    print("It is a vegetable.")
    # You're not supposed to let the program end, so ask the user to select an option instead of return
    return
elif seeds == EXIT:
    sys.exit()

else:
    # Maybe ask the user to retry, it's up to you
    print("Unexeptected input")


# second option
def red():
# clear the screen
os.system('cls')
red = input("Is it red?\n1. yes 2. no: ")
# old code
#   if red == option1:
#     return round()
#   if red == option2:
#     orange()
#   return red
# red(option1, option2)

if red == YES:
    myround()
elif red == NO:
    orange()

elif red == PREV:
    seeds()
elif red == START_OVER:
    seeds()
elif red == EXIT:
    sys.exit()

else:
    print("Unexeptected input")


def orange():
# clear the screen
os.system('cls')
orange = input("Is it orange?\n1. yes 2. no")
# if orange == "1":
#   print("It is an orange.")
#   sys.exit()
# if orange == "2":
#   return yellow()

if orange == YES:
    print("It is an orange.")
    # You're not supposed to let the program end, so ask the user to select an option instead of return
    return
elif orange == NO:
    # call yellow here - implement yellow yourself
    # yellow()
    pass

elif orange == PREV:
    red()
elif orange == START_OVER:
    seeds()
elif orange == EXIT:
    sys.exit()

else:
    print("Unexeptected input")


def myround():
# clear the screen
os.system('cls')
round = input("Is it round?\n1. yes 2. no")
# if round == option1:
#   print("It is an apple.")
#   sys.exit()
# if round == option2:
#   print("It is a strawberry.")
#   sys.exit()

if round == YES:
    print("It is an apple.")
    # You're not supposed to let the program end, so ask the user to select an option instead of return
    return
elif round == NO:
    print("It is a strawberry.")
    # You're not supposed to let the program end, so ask the user to select an option instead of return
    return

elif round == PREV:
    red()
elif round == START_OVER:
    seeds()
elif round == EXIT:
    sys.exit()

else:
    print("Unexeptected input")


def handelInput(input:str)



# Other stuff, implement it yourself following the abouve
# def yellow():
#   yellow = input("Is it yellow?\n1. yes 2. no")
#   if yellow == "1":
#     print("It is a banana")
#     sys.exit()
#   if yellow == "2":
#     return green()
# yellow = yellow()
#
# def green():
#   green = input("Is it green?\n1. yes 2. no")
#   if green == "1":
#     return hairy()
#   if green == "2":
#     return blue()
# green = green()
#
# def hairy():
#   hairy = input("Is it hairy on the outside?\n1. yes 2. no")
#   if hairy == "1":
#     print("It is a kiwi.")
#     sys.exit()
#   if hairy == "2":
#     print("It is a lime.")
#     sys.exit()
# hairy = hairy()
#
# def blue():
#   blue = input("Is it blue?\n1. yes 2. no")
#   if blue == "1":
#     print("It is a blueberry.")
#     sys.exit()
#   if blue == "2":
#     return purple()
# blue =  blue()
#
# def purple():
#   purple = input("Is it purple?\n1. yes 2. no")
#   if purple == "1":
#     print("It is a grape.")
#     sys.exit()
#   if purple == "2":
#     return
# purple = purple()


# ------ running the program -----
seeds()
