#<METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "FishFrenzy"
PROBLEM_VERSION = "1.0"
AUTHORS = ['Anders C.', 'Dawson H.', 'Ren C.', 'Will Z.', 'Mason C.']
CREATION_DATE = "06-SEP-2022"
DESC = ""
#</METADATA>

#<COMMON_CODE>
import random as r
class State:
    def __init__(self, old=None):
        if not old is None:
            self.biodiversityScore = old.biodiversityScore
            self.biodiversityIndex = old.biodiversityIndex
            self.money = old.money
            self.codNum = old.codNum
            self.herringNum = old.herringNum
            self.roundsLeft = old.roundsLeft
            self.fishList = old.fishList
        
        self.biodiversityScore = 100
        self.money = 0
        self.codNum = 100
        self.herringNum = 300
        self.roundsLeft = 12
        self.biodiversityIndex = 0
        self.fishList = [salmon, tuna, cod, pompano, stripedBass, halibut]


    def can_move(self, method):
        if method != 0 and self.codNum <= 0 and self.herringNum <= 0:
            return False
        return True
    
    def fishing_method(self, method):
      if method == 0: #longlines
        return
      elif method == 1: #gillnets
        return
      elif method == 2: #purse seines
        return
      elif method == 3: #trawling
        return 

    def move(self, method):
        #Creates a new state if it is legal
        newState = State(old=self) # Make a copy of the current state.
        newState.roundsLeft = self.roundsLeft - 1
        fish1Caught = 0
        fish2Caught = 0
        self.fishing_method(method)
        if method == 1:
          fish1Caught = r.randint(20, 30)
          fish2Caught = r.randint(60, 80)
        elif method == 2:
          fish1Caught = r.randint(20, 40)
          fish2Caught = r.randint(40, 80)
        
        fish1inOcean = max(self.codNum - fish1Caught, 0)
        fish2inOcean = max(self.herringNum - fish2Caught, 0)
        profit = ((self.codNum - fish1inOcean) * 10 + (self.herringNum - fish2inOcean) * 3)
        
        # A flat rate of multiplying every three rounds and cap at a high num
        newState.fishList = self.fishList
        if (newState.roundsLeft % 3 == 0):
          for f in newState.fishList:
            f.reproduce()
        
        #Ignore this block of code 
        #Calculation of Simpson's Diversity Index
        N = (fish1inOcean + fish2inOcean)
        nSum = fish1inOcean * (fish1inOcean - 1) + fish2inOcean * (fish2inOcean - 1)
        if N > 1:
          newState.biodiversityIndex = round(1.0 - nSum / (N * (N-1)), 3)
        else:
          newState.biodiversityIndex = 1.0
        
        '''fishList = [fish1inOcean, fish2inOcean]
        speciesLeft = len(fishList)
        scoreMultiplier = (100.0 / speciesLeft)
        for f in fishList:
          if f == 0:
            speciesLeft -= 1
        newState.biodiversityScore = (1 - newState.biodiversityIndex) * speciesLeft * scoreMultiplier'''
        
        newState.money += profit
        return newState

    def describe_state(self):
        return

    def is_goal(self):
        if self.roundsLeft == 0:
          return True
        return False
    
    def __eq__(self, s2):
        if s2==None: return False
        if self.money != s2.money: return False
        if self.biodiversityScore != s2.biodiversityScore: return False
        if self.biodiversityIndex != s2.biodiversityIndex: return False
        if self.codNum != s2.codNum: return False
        if self.herringNum != s2.herringNum: return False
        return True

    def __str__(self):
      currentState = '(Profit: '+str(self.money)
      currentState += ', Biodiversity Index: '+str(self.biodiversityIndex)
      currentState += ', Biodiversity Score: '+str(self.biodiversityScore)
      for fish in self.fishList:
        currentState += ', ' + fish.name +' left: '+str(fish.number)
      currentState += ')'
      return currentState

    def __hash__(self):
      return (str(self)).__hash__()
    
    def goal_message(self):
      return "You have completed the game!"

def copy_state(s):
  return State(old=s)

class Fish:
  def __init__(self, name, price, number, repRate):
    self.name = name
    self.price = price
    self.number = number
    self.repRate = repRate

  def reproduce(self):
    if self.number < 6000:
      self.number += (self.number * self.repRate)
    
salmon = Fish('salmon', 750, 150, 1.5)
tuna = Fish('tuna', 1200, 100, 1.5)
cod = Fish('cod', 75, 1000, 1.5)
pompano = Fish('pompano', 20, 3000, 1.5)
stripedBass = Fish('striped bass', 480, 500, 1.5)
halibut = Fish('halibut', 6000, 20, 1.5)

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)
#</COMMON_CODE>

#<INITIAL_STATE>
INITIAL_STATE = State()
#</INITIAL_STATE>

#<OPERATORS>
phi0 = Operator("Do nothing",
  lambda s: s.can_move(0),
  lambda s: s.move(0))

phi1 = Operator("Using a net for more than one fish species",
  lambda s: s.can_move(1),
  lambda s: s.move(1))

phi2 = Operator("Using longlines for more than one fish species",
  lambda s: s.can_move(2),
  lambda s: s.move(2))

OPERATORS = [phi0, phi1, phi2]
#</OPERATORS>