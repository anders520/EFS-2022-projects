#<METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "FishFrenzy"
PROBLEM_VERSION = "1.0"
AUTHORS = ['Anders C.', 'Dawson H.', 'Ren C.', 'Will Z.', 'Mason C.']
CREATION_DATE = "06-SEP-2022"
DESC = ""
#</METADATA>

#<COMMON_CODE>
class State:
    def __init__(self, old=None):
        if not old is None:
            self.biodiversityScore = old.biodiversityScore
            self.biodiversityIndex = old.biodiversityIndex
            self.money = old.money
            self.roundsLeft = old.roundsLeft
            self.fishList = old.fishList
            self.event = old.event
            self.bycatch = old.bycatch
        
        self.biodiversityScore = 100
        self.money = 0
        self.roundsLeft = 12
        self.biodiversityIndex = 0
        self.fishList = [salmon, tuna, cod, pompano, stripedBass, halibut]
        self.event = 0
        self.bycatch = 0


    def can_move(self, method, species):
      if species < 6:
        if method != 0 and self.fishList[species].number <= 0:
          return False
      else:
        if method != 0 and self.fishList[0].number <= 0 and self.fishList[1].number <= 0 and self.fishList[2].number <= 0\
        and self.fishList[3].number <= 0 and self.fishList[4].number <= 0 and self.fishList[5].number <= 0:
          return False
      return True
    
    def fishing_method(self, method, species):
      if method == 1 and species != 3 and species != 5: #longlines targets specific species except for halibut and pompano
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
        if species == 6:
          self.fishList[2].number -= 4000
          self.fishList[5].number -= 4000
          self.bycatch += 2000
          return 4000 * self.fishList[2].price + 4000 * self.fishList[5].price
        self.fishList[species].number -= 4000
        return 4000 * self.fishList[species].price
      elif method == 5: #rod-and-reel
        if species == 6:
          self.fishList[2].number -= 1000
          self.fishList[4].number -= 1000
          self.bycatch += 0
          return 1000 * self.fishList[2].price + 1000 * self.fishList[4].price
        self.fishList[species].number -= 1000
        return 1000 * self.fishList[species].price
      else: #if method == 0: do nothing 
        return 0
        

    def move(self, method, species):
        #Creates a new state if it is legal
        newState = State(old=self) # Make a copy of the current state.
        newState.roundsLeft = self.roundsLeft - 1
        N = 0
        nSum = 0
        newState.biodiversityScore = self.biodiversityScore
        newState.biodiversityIndex = self.biodiversityIndex
        newState.money = self.money
        newState.fishList = self.fishList
        newState.event = self.event
        profit = newState.fishing_method(method, species)

        # A flat rate of multiplying every three rounds and cap at a high num
        if (newState.roundsLeft % 3 == 1):
          for f in newState.fishList:
            f.reproduce()
        
        for fish in newState.fishList:
          fish.number = max(0, fish.number)
          fish.number = min(10000, fish.number)

          N += (fish.number)
          nSum += fish.number * (fish.number - 1)
        
        if (newState.roundsLeft % 3 == 0):
          newState.event = 1
        else:
          newState.event = 0

        if newState.event == 1:
          for f in newState.fishList:
            f.number -= 1000
        #Ignore this block of code 
        #Calculation of Simpson's Diversity Index
        if N > 1:
          newState.biodiversityIndex = round(1.0 - nSum / (N * (N-1)), 3)
        else:
          newState.biodiversityIndex = 1.0
        
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
        return True

    def __str__(self):
      currentState = '(Profit: '+ str(int(self.money / 1000.0)) + 'k'
      currentState += ', Biodiversity Index: '+str(self.biodiversityIndex)
      currentState += ', Biodiversity Score: '+str(self.biodiversityScore)
      for fish in self.fishList:
        currentState += ', ' + fish.name +' left: '+str(fish.number)
      currentState += ')'
      if self.event == 0:
        currentState += '\nThere is no event occuring.'
      elif self.event == 1:
        currentState += '\nA factory had released tons of pollution into the ocean and some fish populations are decreased'  
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
    if self.number < 10000:
      self.number += int(self.number * self.repRate)
    
salmon = Fish('salmon', 750, 6000, 1)
tuna = Fish('tuna', 1200, 6000, 1)
cod = Fish('cod', 75, 6000, 1)
pompano = Fish('pompano', 20, 6000, 1)
stripedBass = Fish('striped bass', 480, 6000, 1)
halibut = Fish('halibut', 6000, 6000, 1)

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

phi5 = Operator("Use longlines to fish Halibut",
  lambda s: s.can_move(1, 5),
  lambda s: s.move(1, 5))
  
phi6 = Operator("Use gill nets to fish Salmon",
  lambda s: s.can_move(2, 0),
  lambda s: s.move(2, 0))

phi7 = Operator("Use gill nets to fish Cod",
  lambda s: s.can_move(2, 2),
  lambda s: s.move(2, 2))

phi8 = Operator("Use gill nets to fish Pompano",
  lambda s: s.can_move(2, 3),
  lambda s: s.move(2, 3))

phi9 = Operator("Use purse seines to fish Salmon",
  lambda s: s.can_move(3, 0),
  lambda s: s.move(3, 0))

phi10 = Operator("Use purse seines to fish Tuna",
  lambda s: s.can_move(3, 1),
  lambda s: s.move(3, 1))

phi11 = Operator("Use trawling to fish Cod",
  lambda s: s.can_move(4, 2),
  lambda s: s.move(4, 2))

phi12 = Operator("Use trawling to fish Halibut",
  lambda s: s.can_move(4, 5),
  lambda s: s.move(4, 5))

phi13 = Operator("Use trawling to fish Cod and Halibut",
  lambda s: s.can_move(4, 6),
  lambda s: s.move(4, 6))

phi14 = Operator("Use rod and reel for Cod and Striped Bass",
  lambda s: s.can_move(5, 6),
  lambda s: s.move(5, 6))

phi15 = Operator("Use rod and reel to fish for Salmon",
  lambda s: s.can_move(5, 0),
  lambda s: s.move(5, 0))

phi16 = Operator("Use rod and reel to fish for Tuna",
  lambda s: s.can_move(5, 1),
  lambda s: s.move(5, 1))
  
phi17 = Operator("Use rod and reel to fish for Cod",
  lambda s: s.can_move(5, 2),
  lambda s: s.move(5, 2))

phi18 = Operator("Use rod and reel to fish for Pompano",
  lambda s: s.can_move(5, 3),
  lambda s: s.move(5, 3))

phi19 = Operator("Use rod and reel to fish for Striped Bass",
  lambda s: s.can_move(5, 4),
    lambda s: s.move(5, 4))

phi20 = Operator("Use rod and reel to fish for Halibut",
  lambda s: s.can_move(5, 5),
  lambda s: s.move(5, 5))

OPERATORS = [phi0, phi1, phi2, phi3, phi4, phi5, phi6, phi7, phi8, phi9, phi10, phi11, phi12,\
   phi13, phi14, phi15, phi16, phi17, phi18, phi19, phi20]
#</OPERATORS>