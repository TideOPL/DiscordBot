import random
import time

repeat = input("(!) Would you like to initialize the game loop? (Yes or No): ")
time.sleep(2)

if repeat == "Yes":
    print("(!) The game will now repeat!")
    running = True

player1 = input("(!) What would you like Player 1's name to be?: ")
player2 = input("(!) Player 2 name: ")


def maingameloop():
    play = input("Would you like to roll? (Yes or No): ")
    pl1 = random.randrange(0,7)
    pl2 = random.randint(0, 7)


    if play == "Yes":
        print("(!) Rolling!")
        time.sleep(1)
        print("(!)", player1 + "'s number is:", pl1,)
        time.sleep(0.5) 
        print("(!)", player2 + "'s number is:", pl2)
    if play == "No":
        quit()

if repeat == "No":
    print("(!) After your first role you will have to relaunch the game!")
    maingameloop()



while running:
    maingameloop()
