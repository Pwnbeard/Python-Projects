import sys
import random

first = ("Dougy", "Beaty", "Juggalo", "Jimbo", "Albertrum", "Shakhma")

last = ("Longbuns", "Hammerdome", "Toothgrabber", "Bungletron",
        "Numptyneck", "Smith")

while True:
    Rfirst = random.choice(first)
    Rlast = random.choice(last)

    Rname = Rfirst + " " + Rlast

    print("{} {}".format(Rfirst, Rlast), file=sys.stderr)
    tryagain = input("\n Try Again? (ENTER to go again, n to quit)\n")
    if tryagain.lower() == "n":
        break
