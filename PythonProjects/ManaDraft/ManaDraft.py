import numpy as np

# Create necessary blank lists
colors = []
totalpips = []
LC = []


# Collect information, append list if color does not = 0
def ManaDraft():
    lands = int(input("How many lands in your deck?"))
    LC.append(lands)
    wpip = int(input("How many WHITE pips in your deck?"))
    if wpip > 0:
        colors.append("WHITE")
        totalpips.append(wpip)
    bpip = int(input("How many BLACK pips in your deck?"))
    if bpip > 0:
        colors.append("BLACK")
        totalpips.append(bpip)
    upip = int(input("How many BLUE pips in your deck?"))
    if upip > 0:
        colors.append("BLUE")
        totalpips.append(upip)
    rpip = int(input("How many RED pips in your deck?"))
    if rpip > 0:
        colors.append("RED")
        totalpips.append(rpip)
    gpip = int(input("How many GREEN pips in your deck?"))
    if gpip > 0:
        colors.append("GREEN")
        totalpips.append(gpip)
    # Summarize, review, and verify inputs to continue
    pipsum = sum(totalpips)
    print("You want to use " + str(lands) + " total lands")
    print("Your deck's colors are: " + str(colors))
    print("Your deck contains " + str(pipsum) + " pips in total")
    prompt()


# Verification
def prompt():
    proceed = input("Is this correct? Y/N: ")
    if proceed.lower() == "n" or proceed.lower == "no":
        print("Let's start again.")
        ManaDraft()
    elif proceed.lower() == "y" or proceed.lower == "yes":
        print("Beginning calculation")
        calculate()
    else:
        print("Invalid selection")
        prompt()


# Calculate mana base from pips
def calculate():
    colorarr = np.array(colors)
    piparr = np.array(totalpips)
    pipsum = sum(totalpips)
    ratios = np.array(piparr/pipsum)
    print(colorarr)
    print(ratios)
    LCrat = np.array(ratios*LC)
    LCfloor = np.floor(LCrat)
    print(LCfloor)
    if np.sum(LCfloor) != LC:
        remainder = LC - np.sum(LCfloor)
        print(f"Wild Lands: {remainder}")
    print("All Done!")
    input("Press any key to end")


print("""
Welcome to ManaDraft!
This tool is designed to streamline
your mana numbers for drafts
so you spend more time building
and playing and less time doing math!
""")
input("Press any key to continue")
ManaDraft()
