# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:46:19 2019

@author: ditto
"""


def prompt():  # Menu blocks
    input("Press ENTER to continue")


def select():
    print("Make your selection:")
    print("1. Nice")
    print("2. Blaze")
    print("3. Belt")
    print("4. Monster")

    choice = input("Enter choice: ")
    if choice == "Nice" or choice == "1" or choice == "nice":
        a = int(input("Choose a number: "))
        nice(a)
        loop()
    elif choice == "Blaze" or choice == "2" or choice == "blaze":
        it = int(input("What number shall we burn? "))
        blaze(it)
        loop()
    elif choice == "Belt" or choice == "3" or choice == "belt":
        strength = int(input("Strength: "))
        stamina = int(input("Stamina: "))
        belt(strength, stamina)
        loop()
    elif choice == "Monster" or choice == "4" or choice == "monster":
        num_mon = float(input("Choose a dollar amount(x.xx): "))
        monster(num_mon)
        loop()
    else:
        print("Try again, mortal")
        select()


def loop():
    prompt()
    select()


def nice(a):  # Diabolic Functions
    if a != 69:
        print(int(69-a)+(a))
    else:
        print("Nice!")


def monster(num_mon):
    if num_mon < 3.50:
        needed = (3.50-num_mon)
        print("That's not enough!")
        print("I need about ", round(needed, 2), " more")
        loop()
    elif num_mon > 3.50:
        needed = (num_mon-3.50)
        print("That's too much!")
        print("I need about", round(needed, 2), " less")
        loop()
    else:
        print("Thank you! \nThat's just about how much I needed!")
        loop()


def blaze(it):
    if it != 1 and 420 % it == 0 or 420 % it == 1:
        print("Can be blazed!")
    else:
        print("Cannot be blazed!")


def belt(strength, stamina):
    if strength < 4:
        print("Not enough strength!")
        if stamina < 4:
            print("Not enough stamina!")
        elif stamina > 4:
            print("Too much stamina!")
        else:
            print("Just the right amount of stamina!")
        loop()
    elif strength > 4:
        print("Too much strength!")
        if stamina < 4:
            print("Not enough stamina!")
        elif stamina > 4:
            print("Too much stamina!")
        else:
            print("Just the right amount of stamina!")
        loop()
    else:
        print("Belt, leather belt!")
        print("4 strength 4 stam!")
        print("OH DUDE! LEVEL 18!")


print(
    """Welcome to the Diabolic Calculator!
The goal of this puzzle is to figure out
what each unusual operation does.
All inputs are required to be one or more numbers
but not all outputs will be numbers."""
)

loop()
