import random
import os
import time


def prompt():
    input("Press ENTER to continue")


def cl():  # chirp loop (cl)
    while True:
        global num
        num = [random.randint(1, 5)]
        print("chirp" + str(".") * num[0])
        time.sleep(2)


def al():  # action loop (al)
    action = input("Wat do?").lower()
    if action == "wap" and num[0] == 1:
        print("""
        GUD WERK!
        YOU WAP DUM BURD GUD!
        VICTORY IS YOURS THIS DAY!
        """)
        prompt()
    if action != "wap":
        print("You spell wap wrong")
    else:
        print("You no hit dum burd. Try again!")


def mainloop():  # main process loop
    f = os.fork()
    if f > 0:
        al()
    else:
        cl()


def welcome():
    print("""
Welcome to chirp/whap!
You are a cat
Want whap dum burd
Sometimes burd close (chirp.)
Sometimes burd far (chirp.....)
Type wap and press ENTER to wap dum burd
But ONLY when dum burd close
    """)
    prompt()
    mainloop()


welcome()
