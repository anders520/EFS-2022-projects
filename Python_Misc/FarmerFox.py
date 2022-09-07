#<METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "The Farmer, the Fox, the Chicken, and the Grain"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['D. Harris', 'A. Choy']
PROBLEM_CREATION_DATE = "31-AUG-2022"
PROBLEM_DESC=\
'''Similar to Missionaries and Cannibals. Player must get everything
across the river. Farmer must row the boat across the river or alone with
one of the animals or the grain.
Constraints incluide: Fox must not be left alone with the chicken or chicken gets eaten.
Chicken must not be alone or the grain gets eaten.
'''
#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>
#frmr=0  # array index to access farmer location (0 means left, 1 means right)
#fox=0   # same idea for fox
#c=0     # same idea for chicken
#g=0     # same idea for grain
#b=0     # Boat is on left when 0, right when 1

class gameState:
  def __init__(self, old=None):
    self.farmerLocation = 0
    self.foxLocation = 0
    self.chickenLocation = 0
    self.grainLocation = 0
    if not old is None:
      self.farmerLocation = old.farmerLocation
      self.foxLocation = old.foxLocation
      self.chickenLocation = old.chickenLocation
      self.grainLocation = old.grainLocation
      self.boatLocation = old.boatLocation
    else:
      self.boatLocation = 0

  def can_move(self,frmr,fox,c,g):
    # Tests whether it's legal to move the boat and take the animals or grain.
    boatSide = self.boatLocation # Where the boat is.
    # The Farmer is required to steer boat.
    farmerLoc = abs(frmr - self.farmerLocation)
    foxLoc = abs(fox - self.foxLocation)
    chickenLoc = abs(c - self.chickenLocation)
    grainLoc = abs(g - self.grainLocation)
    if foxLoc == chickenLoc and farmerLoc != foxLoc: return False
    if chickenLoc == grainLoc and farmerLoc != chickenLoc: return False
    else: return True

  def move(self,frmr,fox,c,g):
    #Creates a new state if it is legal to move the farmer and an animal or grain.
    newState = gameState(old=self) # Make a copy of the current state.
    boatSide = self.boatLocation
    if boatSide:
      newState.foxLocation -= fox
      newState.chickenLocation -= c
      newState.grainLocation -= g
    else:
      newState.foxLocation += fox
      newState.chickenLocation += c
      newState.grainLocation += g
    newState.boatLocation = 1-boatSide     # Moves the boat
    newState.farmerLocation = newState.boatLocation
    return newState

  def describe_state(self):
    # Produces a textual description of a state.
    # Might not be needed in normal operation with GUIs.
    frmrInt = self.farmerLocation
    foxInt = self.foxLocation
    cInt = self.chickenLocation
    gInt = self.grainLocation
    boatInt = self.boatLocation
    
    if frmrInt == 1:
        farmerSide = 'Right'
    else:
        farmerSide = 'Left'

    if foxInt == 1:
        foxSide = 'Right'
    else:
        foxSide = 'Left'

    if cInt == 1:
        chickenSide = 'Right'
    else:
        chickenSide = 'Left'

    if gInt == 1:
        grainSide = 'Right'
    else:
        grainSide = 'Left'

    if boatInt == 1:
        boatSide = 'Right'
    else:
        boatSide = 'Left'

    txt = "The Farmer is on the " + farmerSide+"\n"
    txt += "The Fox is on the " + foxSide+"\n"
    txt += "The Chicken is on the " + chickenSide+"\n"
    txt += "The Grain is on the " + grainSide+"\n"
    txt += "The boat is on the "+boatSide+".\n"
    return txt

  def is_goal(self):
    #If everything is on the right, then s is the goal state.
    frmrInt = self.farmerLocation
    foxInt = self.foxLocation
    cInt = self.chickenLocation
    gInt = self.grainLocation
    return (frmrInt+foxInt+cInt+gInt==4)

  def __eq__(self, s2):
    if s2==None: return False
    if self.boatLocation != s2.boatLocation: return False
    if self.farmerLocation != s2.farmerLocation: return False
    if self.foxLocation != s2.foxLocation: return False
    if self.chickenLocation != s2.chickenLocation: return False
    if self.grainLocation != s2.grainLocation: return False
    return True

  def __str__(self):
    currentState = '('+str(self.farmerLocation)
    currentState += ','+str(self.foxLocation)
    currentState += ','+str(self.chickenLocation)
    currentState += ','+str(self.grainLocation)
    currentState += ','+str(self.boatLocation)+')'
    return currentState

  def __hash__(self):
    return (str(self)).__hash__()

  def goal_message(self):
    return "Congratulations on successfully guiding the"+\
           " Farmer, Fox, Chicken, and Grain across the river!"

def copy_state(s):
  return gameState(old=s)

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
INITIAL_STATE = gameState()
#</INITIAL_STATE>

#<OPERATORS>
phi0 = Operator("Cross the river with the Farmer",
  lambda s: s.can_move(1,0,0,0),
  lambda s: s.move(1,0,0,0))

phi1 = Operator("Cross the river with the Farmer and the Fox",
  lambda s: s.can_move(1,1,0,0),
  lambda s: s.move(1,1,0,0))

phi2 = Operator("Cross the river with the Farmer and the Chicken",
  lambda s: s.can_move(1,0,1,0),
  lambda s: s.move(1,0,1,0))

phi3 = Operator("Cross the river with the Farmer and the Grain",
  lambda s: s.can_move(1,0,0,1),
  lambda s: s.move(1,0,0,1))

OPERATORS = [phi0, phi1, phi2, phi3]
#</OPERATORS>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>