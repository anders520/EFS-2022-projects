#<METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "FishFrenzy"
PROBLEM_VERSION = "1.0"
AUTHORS = ['Anders C.', 'Dawson H.', 'Ren C.', 'Will Z.', 'Mason C.']
CREATION_DATE = "06-SEP-2022"
DESC = ""
#</METADATA>

#<COMMON_CODE>
import sys
class Fish:
  def __init__(self, name, price, number, repRate):
    self.name = name
    self.price = price
    self.number = number
    self.repRate = repRate

  def reproduce(self):
    if self.number < 10000:
      self.number += int(self.number * self.repRate)

class State:
    def __init__(self, old=None):
      self.salmon = Fish('Salmon', 750, 6000, 0.5)
      self.tuna = Fish('Tuna', 1200, 6000, 0.5)
      self.cod = Fish('Cod', 75, 6000, 0.5)
      self.pompano = Fish('Pompano', 20, 6000, 0.5)
      self.stripedBass = Fish('Striped Bass', 480, 6000, 0.5)
      self.halibut = Fish('Halibut', 6000, 6000, 0.5)
      self.biodiversityScore = 100
      self.money = 0
      self.roundsLeft = 20
      self.biodiversityIndex = 0
      self.fishList = [self.salmon, self.tuna, self.cod, self.pompano, self.stripedBass, self.halibut]
      self.event = 0
      self.bycatch = 0
      self.nothing = 0   
      if not old is None:
          self.biodiversityScore = old.biodiversityScore
          self.biodiversityIndex = old.biodiversityIndex
          self.money = old.money
          self.roundsLeft = old.roundsLeft
          self.fishList = old.fishList
          self.event = old.event
          self.bycatch = old.bycatch 
          self.nothing = old.nothing


    def can_move(self, method, species):
      if self.biodiversityScore < 75 or self.nothing >= 4: return False
      if method == 6: return True
      if species < 6:
        if method != 0 and self.fishList[species].number <= 0:
          return False
      else:
        if method != 0 and self.fishList[2].number <= 0:
          return False
      return True
    
    def fishing_method(self, method, species):
      if method == 6:
        psum = 0
        for f in self.fishList:
          psum += f.number * f.price
          f.number -= f.number
        return psum
      elif method == 1 and species != 3 and species != 5: #longlines targets specific species except for halibut and pompano
        self.fishList[species].number -= 2000
        self.bycatch += 200
        return 2000 * self.fishList[species].price
      elif method == 2: #gillnets
        self.fishList[species].number -= 3000
        self.bycatch += 500
        return 3000 * self.fishList[species].price
      elif method == 3: #purse seines
        self.fishList[species].number -= 3000
        self.bycatch += 1000
        return 3000 * self.fishList[species].price
      elif method == 4: #trawling
        self.fishList[2].number -= 4000
        self.fishList[5].number -= 4000
        self.bycatch += 2000
        return 4000 * self.fishList[2].price + 4000 * self.fishList[5].price
      elif method == 5: #rod-and-reel
        if species == 6:
          self.fishList[2].number -= 1000
          self.fishList[4].number -= 1000
          self.bycatch += 0
          return 1000 * self.fishList[2].price + 1000 * self.fishList[4].price
        self.fishList[species].number -= 1000
        return 1000 * self.fishList[species].price
      else: #if method == 0: do nothing 
        self.nothing += 1
        return 0
        

    def move(self, method, species):
        #Creates a new state if it is legal
        newState = State(old=self) # Make a copy of the current state.
        newState.roundsLeft = self.roundsLeft - 1
        N = 0
        nSum = 0
        self.fishList = [Fish('Salmon', 750, self.fishList[0].number, 0.5), Fish('Tuna', 1200, self.fishList[1].number, 0.5), Fish('Cod', 75, self.fishList[2].number, 0.5), Fish('Pompano', 20, self.fishList[3].number, 0.5), Fish('Striped Bass', 480, self.fishList[4].number, 0.5), Fish('Halibut', 6000, self.fishList[5].number, 0.5)]
        profit = newState.fishing_method(method, species)

        # A flat rate of multiplying every three rounds and cap at a high num
        if (newState.roundsLeft % 4 == 1):
          for f in newState.fishList:
            f.reproduce()
        
        for fish in newState.fishList:
          fish.number = min(10000, fish.number)
          
        if (newState.roundsLeft == 16 or newState.roundsLeft == 10 or newState.roundsLeft == 4):
          newState.event = 1
        elif (newState.roundsLeft == 13 or newState.roundsLeft == 7):
          newState.event = 2
        else:
          newState.event = 0

        if newState.event == 1:
          for f in newState.fishList:
            f.number -= 1000
        elif newState.event == 2:
          for f in newState.fishList:
            f.number -= 500
        
        for fish in newState.fishList:
          fish.number = max(0, fish.number)

          N += (fish.number)
          nSum += fish.number * (fish.number - 1)
        N += max(0, 10000 - newState.bycatch)
        nSum += (max(0, 10000 - newState.bycatch)) * (max(0, 10000 - newState.bycatch) - 1)
        #Ignore this block of code 
        #Calculation of Simpson's Diversity Index
        if N > 1:
          newState.biodiversityIndex = round(1.0 - nSum / (N * (N-1)), 3)
        else:
          newState.biodiversityIndex = 0.0
        divIndex = round(1 - (((6000 * 5999 * 6) + (10000 * 9999)) / (46000 * 45999)), 3)
        newState.biodiversityScore = round((newState.biodiversityIndex / divIndex) * 100, 1)
        newState.money += profit
        return newState

    #def describe_state(self):
        #return

    def is_goal(self):
        if self.roundsLeft == 0:
          return True
        return False
    
    def __eq__(self, s2):
        if s2==None: return False
        if self.money != s2.money: return False
        if self.biodiversityScore != s2.biodiversityScore: return False
        if self.biodiversityIndex != s2.biodiversityIndex: return False
        if self.roundsLeft != s2.roundsLeft: return False
        if self.fishList != s2.fishList: return False
        if self.event != s2.event: return False
        if self.bycatch != s2.bycatch: return False
        return True
    
    def date(self):
      date = ''
      if self.roundsLeft >= 17:
        date = '\nYear 2025 Quarter ' + str(21 - self.roundsLeft)
      elif self.roundsLeft >= 13:
        date = '\nYear 2026 Quarter ' + str(17 - self.roundsLeft)
      elif self.roundsLeft >= 9:
        date = '\nYear 2027 Quarter ' + str(13 - self.roundsLeft)
      elif self.roundsLeft >= 5:
        date = '\nYear 2028 Quarter ' + str(9 - self.roundsLeft)
      elif self.roundsLeft >= 1:
        date = '\nYear 2029 Quarter ' + str(5 - self.roundsLeft)
      return date
        
    def __str__(self):
      kill = False
      currentState = '(Gross Profit: '+ str(int(self.money / 1000.0)) + 'k'
      currentState += ', Biodiversity Index: '+str(self.biodiversityIndex)
      currentState += ', Biodiversity Score: '+str(self.biodiversityScore)
      for i in range(len(self.fishList)):
        if (i % 3 == 0):
          currentState += ', \n' + self.fishList[i].name +' left: '+str(self.fishList[i].number)
        else:
          currentState += ', ' + self.fishList[i].name +' left: '+str(self.fishList[i].number)
      #for fish in self.fishList:
        #currentState += ', \n' + fish.name +' left: '+str(fish.number)
      currentState += ', \nBycatch: '+str(self.bycatch)
      currentState += ')'
      currentState += self.date()
      if self.roundsLeft == 20:
        currentState += '''

Welcome to Fishing Frenzy! You are the new decision maker of WARMD Fishing Co.
There are different fishing methods you can use to earn profit for the company. 
Your goal is to earn as much as possible while keeping the ecosystem healthy meaning that your Biodiversity Score cannot drop below 75.
Good Luck and Have Fun!
'''
      if self.biodiversityScore == 0:
        currentState += '\nCongratulations, all fish have been killed by YOU... YOU LOST!!!'
        kill = True
      elif self.biodiversityScore < 75: currentState += '\nYou have lost the game because your Biodiversity Score is \
lower than 75, and you can only quit the game no...'
      elif self.nothing == 4:
        currentState += '\nYou were fired for not fishing for multiple rounds!'
      elif self.event == 0:
        currentState += '\nThere is no event occuring.'
      elif self.event == 1:
        currentState += '\nA factory had released tons of pollution into the ocean and fish populations are decreased by 1000'
      elif self.event == 2:
        currentState += '\nA hurricane caused runoff pollution and fish populations are decreased by 500'
      #if kill:
        #sys.exit(currentState)
      return currentState

    def __hash__(self):
      return (str(self)).__hash__()
    
    def goal_message(self):
      return "You have completed the game!"

def copy_state(s):
  return State(old=s)
def goal_test(self):
        if self.roundsLeft == 0:
          return True
        return False

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
  lambda s: s.can_move(0, 0),
  lambda s: s.move(0, 0))

phi1 = Operator("Use longlines to fish Salmon",
  lambda s: s.can_move(1, 0),
  lambda s: s.move(1, 0))

phi2 = Operator("Use longlines to fish Tuna",
  lambda s: s.can_move(1, 1),
  lambda s: s.move(1, 1))

phi3 = Operator("Use longlines to fish Cod",
  lambda s: s.can_move(1, 2),
  lambda s: s.move(1, 2))

phi4 = Operator("Use longlines to fish Striped Bass",
  lambda s: s.can_move(1, 4),
  lambda s: s.move(1, 4))
  
phi5 = Operator("Use gill nets to fish Salmon",
  lambda s: s.can_move(2, 0),
  lambda s: s.move(2, 0))

phi6 = Operator("Use gill nets to fish Cod",
  lambda s: s.can_move(2, 2),
  lambda s: s.move(2, 2))

phi7 = Operator("Use gill nets to fish Pompano",
  lambda s: s.can_move(2, 3),
  lambda s: s.move(2, 3))

phi8 = Operator("Use purse seines to fish Salmon",
  lambda s: s.can_move(3, 0),
  lambda s: s.move(3, 0))

phi9 = Operator("Use purse seines to fish Tuna",
  lambda s: s.can_move(3, 1),
  lambda s: s.move(3, 1))

phi10 = Operator("Use trawling to fish Cod and Halibut",
  lambda s: s.can_move(4, 6),
  lambda s: s.move(4, 6))

phi11 = Operator("Use rod and reel for Cod and Striped Bass",
  lambda s: s.can_move(5, 6),
  lambda s: s.move(5, 6))

phi12 = Operator("Use rod and reel to fish for Salmon",
  lambda s: s.can_move(5, 0),
  lambda s: s.move(5, 0))

phi13 = Operator("Use rod and reel to fish for Tuna",
  lambda s: s.can_move(5, 1),
  lambda s: s.move(5, 1))
  
phi14 = Operator("Use rod and reel to fish for Cod",
  lambda s: s.can_move(5, 2),
  lambda s: s.move(5, 2))

phi15 = Operator("Use rod and reel to fish for Pompano",
  lambda s: s.can_move(5, 3),
  lambda s: s.move(5, 3))

phi16 = Operator("Use rod and reel to fish for Striped Bass",
  lambda s: s.can_move(5, 4),
    lambda s: s.move(5, 4))

phi17 = Operator("Use rod and reel to fish for Halibut",
  lambda s: s.can_move(5, 5),
  lambda s: s.move(5, 5))

phi18 = Operator("Go Bomb fishing",
  lambda s: s.can_move(6, 5),
  lambda s: s.move(6, 5))


OPERATORS = [phi0, phi1, phi2, phi3, phi4, phi5, phi6, phi7, phi8, phi9, phi10, phi11, phi12,\
   phi13, phi14, phi15, phi16, phi17, phi18]
#</OPERATORS>