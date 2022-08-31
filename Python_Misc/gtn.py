import random as r
import time as t
import sys

def guess_the_number():
    tries = 5
    screwed_up = 0
    num = r.randint(1, 100)
    min_limit = 1
    max_limit = 100
    print("Welcome to Guess the number!")
    t.sleep(0.25)
    
    answer = input("Guess a number between 1 and 100! " )
    
    while (tries > 0 and answer != num):
        lst = list(range(1, 101))
        l = ([str(x) for x in lst])
        while answer not in l:
            screwed_up +=1
            if screwed_up < 3:
                answer = input("Enter a number between 1 and 100! ")
            else:
                print("...")
                t.sleep(0.2)
                print("......")
                t.sleep(0.2)
                print(".........")
                t.sleep(0.2)
                print("You are dumb... ")
                sys.exit("NOW GTFO!")
        answer = int(answer)
        tries -= 1
        if answer == num:
            print("Correct! You win!")
            break
        elif answer < num:
            if tries == 0:
                print("You lost! The answer was " + str(num))
                break
            print("Wrong! The number is between " + str(answer) + " and " + str(max_limit))
            min_limit = answer
            answer = input(str(tries) + " tries left... " + "Guess again! ")
        elif answer > num:
            if tries == 0:
                print("You lost! The answer was " + str(num))
                break
            print("Wrong! The number is between " + str(min_limit) + " and " + str(answer))
            max_limit = answer
            answer = input(str(tries) + " tries left... " + "Guess again! ")
    else:
        print("You lost!")

guess_the_number()
    
