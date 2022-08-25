import random as r
from PIL import Image
import glob

list = ['Rock', 'Paper', 'Scissors']
def cpu_rand():
    cpu_num = r.randint(0, 2)
    print("Computer chose: " + str(list[cpu_num]))
    return(int(cpu_num))

def user_num():
    user_num = 0
    user_input = input("Rock/Paper/Scissors? ")
    while (type(user_input) != str):
        user_input = input("Please enter Rock, Paper, or Scissors!")
    if (user_input.lower() == "rock"):
        user_num = 0
    elif (user_input.lower() == "paper"):
        user_num = 1
    elif (user_input.lower() == "scissors"):
        user_num = 2
    else:
        user_input = input("Please enter Rock, Paper, or Scissors!")

    print("You chose: " + user_input.upper())
    return user_num

def play():
    u = user_num()
    c = cpu_rand()
    user_win = 0
    m = max(u, c)
    if (u != c):
        if (u == m):
            if (u - c == 1):
                user_win = 1
            else:
                user_win = 0
        else:
            if (c - u == 1):
                user_win = 0
            else:
                user_win = 1
    else:
        user_win = 2

    return user_win

        

user_wins = 0
cpu_wins = 0
draws = 0
play_again = True
while (play_again == True):
    while user_wins < 2 and cpu_wins < 2:
        win = play()
        if win == 1:
            user_wins += 1
        elif win == 0:
            cpu_wins += 1
        elif win == 2:
            draws += 1
    print('user_wins = ' + str(user_wins) + ', cpu_wins = ' + str(cpu_wins) + ', draws = ' + str(draws))
    if user_wins >= 2:
        print("Congratulations! You Won!")
    if cpu_wins >= 2:
        print("HA! You Lost! Do better la!")
        image = Image.open('./Beijing Corn.png')
        image.show()
            
    rep = input("Play Again? (Y/N) ")
    if (type(rep) == str):
        if (rep.lower() == "y"):
            play_again = True
            print("Here we go again!")
            user_wins = 0
            cpu_wins = 0
            draws = 0
        elif (rep.lower() == "n"):
            play_again = False
            print("Game Over!")
        else:
            play_again = False
            print("Game Over!")
