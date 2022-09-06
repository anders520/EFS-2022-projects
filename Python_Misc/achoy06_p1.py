'''
This file contains the starter code for Project 1 in
CSE 190C, Early Fall Start, 2022.

Edit or complete all the assignment statements,
function definitions, etc., as indicated in the instructions.
'''

UWNetID = "achoy06" # replace with your own UWNetID.
LAST_NAME = "CHOY"   # replace with your own last name.
FIRST_NAME = "ANDERS" # replace with your own first name.

OPTIONAL_PARTNER_LAST_NAME = "HARRIS" # Change this if you have a partner
OPTIONAL_PARTNER_FIRST_NAME = "DAWSON" # Change this if you have a partner

# EXERCISE 1:
#   Note that this one is done for you, so you can see how
#   functions must "return" values, and NOT print them.
def triple(n):
  return 3*n

# EXERCISE 2:
def four_x_squared_plus_seven_x_plus_two(x):
  return((4 * (x * x)) + (7 * x) + 2)

# EXERCISE 3:
def please_repeat_that(something):
  return(str(something) + " -- I said, " + str(something))

# EXERCISE 4:
def roll_die():
  import random as r
  die = r.randint(1, 6)
  return die

# EXERCISE 5:
def twelfth_root(x):
  return x ** (1./12.)

# EXERCISE 6:
def makepal(a_seq):
  reversed_a_seq = a_seq[-1::-1]
  return a_seq + reversed_a_seq
  

# EXERCISE 7:
class Movie:
  def __init__(self, genre, title, director, release_date, language, leading_actors,\
               plot_sum):
    self.genre = genre
    self.title = title
    self.director = director
    self.release_date = release_date
    self.language = language
    self.leading_actors = leading_actors
    self.plot_sum = plot_sum

  def __str__(self):
    return str("Movie with genre " + self.genre + ", title '" + self.title + \
            "', directed by " + self.director + ", released during " + \
            self.release_date + " in " + self.language + ", with leading actors "\
            + ", ".join(self.leading_actors) + "; plot summary: " + self.plot_sum)

def by_genre(movie_list, genre):
  same_genre = []
  for m in movie_list:
    if (m.genre == genre):
      same_genre.append(m)
  return same_genre


# EXERCISE 8:
def is_prime(p):
  if p >= 1:
    for checkIfPrime in range(2, int(p/2)+1):
      if (p % checkIfPrime) == 0:
        return False
    return True
  return False

def does_p_divide_n_minus_m(p, n, m):
  if is_prime(p) and n >= m:
    subtractedNum = n - m
    if subtractedNum % p == 0:
      return True
  return False

def find_the_number():
  import random as r
  print('''Welcome to the Find-the-Number game!
I am thinking of an integer between 0 and 99.
You may ask me questions about it, or try to guess it.
Your score will be 50 minus the number of questions you ask and guesses you make.''')
  n = r.randint(0, 99)
  isCorrect = False
  score = 50
  while not isCorrect:
    user_input = str(input("(A)ask? (G)guess? or (Q)quit? --> "))
    score -= 1
    if user_input.upper() == "A":
      q = input('Enter m, p to ask "Is the number (n) minus m divisible by p?" --> ')
      lq = q.split(",")
      if does_p_divide_n_minus_m(int(lq[1]), n, int(lq[0])):
        print("Yes, n - " + lq[0] + " is divisible by " + lq[1])
      else:
        print("No, n - " + lq[0] + " is not divisible by " + lq[1])
    elif user_input.upper() == "G":
      guess = int(input("What's your guess? --> "))
      if guess == n:
        print("Yes, you guessed it! Your score is "+ str(score) +".\nThanks for playing.")
        isCorrect = True
      else:
        print("Sorry, " + str(guess) + " is not my number.")
    elif user_input.upper() == "Q":
      score = 0
      print("What, you are quitting? OK. My number was " + str(n) + ". Your score is " +\
            str(score) + ".\nYou'll have to try harder in the future.")
      break

