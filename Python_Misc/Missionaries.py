'''Missionaries.py
("Missionaries and Cannibals" problem)
A SOLUZION problem formulation.  UPDATED AUGUST 2018.
The XML-like tags used here may not be necessary, in the end.
But for now, they serve to identify key sections of this 
problem formulation.  It is important that COMMON_CODE come
before all the other sections (except METADATA), including COMMON_DATA.
'''
#<METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "Missionaries and Cannibals"
PROBLEM_VERSION = "0.4"
PROBLEM_AUTHORS = ['S. Tanimoto']
PROBLEM_CREATION_DATE = "1-SEP-2020"
PROBLEM_DESC=\
'''This version differs from earlier ones by (a) using a new
State class to represent problem states, rather than just
a dictionary, and (b) avoidance of list comprehensions
and the use of default parameter values in lambda expressions.

The following are new methods here for the State version of
the formulation:
__eq__, __hash__, __str__, and the implcit constructor State().

The previous version was written to accommodate the
Brython version of the solving client
and the Brython version of Python.
However, everything else is generic Python 3, and this file is intended
to work a future Python+Tkinter client that runs on the desktop.
Anything specific to the Brython context should be in the separate 
file MissionariesVisForBRYTHON.py, which is imported by this file when
being used in the Brython SOLUZION client.

The operators are defined here in the same order as on the
worksheet "Depth-First Search for the M&C Problem."

This version is compatible with the 2020 version of ItrDFS.py, which
gives a more detailed printout of its execution than older versions did.
'''

#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>
#M=0  # array index to access missionary counts
#C=1  # same idea for cannibals
#LEFT=0 # same idea for left side of river
#RIGHT=1 # etc.

class State:
  def __init__(self, old=None):
    # Default new state is a state objects initialized as the
    # initial state.
    # If called with old equal to a non-empty state, then
    # the new instance is made to be a copy of that state.
    self.n_missionaries_on_right = 0
    self.n_cannibals_on_right = 0
    if not old is None:
      self.n_missionaries_on_right = old.n_missionaries_on_right
      self.n_cannibals_on_right = old.n_cannibals_on_right
      self.n_boats_on_right = old.n_boats_on_right
    else:
      self.n_boats_on_right = 0

  def can_move(self,m,c):
    '''Tests whether it's legal to move the boat and take
    m missionaries and c cannibals.'''
    if m<1: return False # Need an M to steer boat.
    side = self.n_boats_on_right # Where the boat is.
    m_available = self.n_missionaries_on_right if side else 3 - self.n_missionaries_on_right
    if m_available < m: return False # Can't take more m's than available
    c_available = self.n_cannibals_on_right if side else 3 - self.n_cannibals_on_right
    if c_available < c: return False # Can't take more c's than available
    m_remaining = m_available - m
    c_remaining = c_available - c
    # Missionaries must not be outnumbered on either side:
    if m_remaining > 0 and m_remaining < c_remaining: return False
    m_at_arrival = 3 - m_available + m
    c_at_arrival = 3 - c_available + c
    if m_at_arrival > 0 and m_at_arrival < c_at_arrival: return False
    return True

  def move(self,m,c):
    '''Assuming it's legal to make the move, this make a new state
    representing the result of moving the boat carrying
    m missionaries and c cannibals.'''
    news = State(old=self) # Make a copy of the current state.
    side = self.n_boats_on_right
    if side:
      news.n_missionaries_on_right -= m
      news.n_cannibals_on_right -= c
    else:
      news.n_missionaries_on_right += m
      news.n_cannibals_on_right += c
    news.n_boats_on_right = 1-side     # Move the boat itself.
    return news

  def describe_state(self):
    # Produces a textual description of a state.
    # Might not be needed in normal operation with GUIs.
    nmr = self.n_missionaries_on_right
    ncr = self.n_cannibals_on_right
    txt = "M on left:"+str(3-nmr)+"\n"
    txt += "C on left:"+str(3-ncr)+"\n"
    txt += "  M on right:"+str(nmr)+"\n"
    txt += "  C on right:"+str(ncr)+"\n"
    side='left'
    if self.n_boats_on_right==1: side='right'
    txt += " boat is on the "+side+".\n"
    return txt

  def is_goal(self):
    '''If all Ms and Cs are on the right, then s is a goal state.'''
    nmr = self.n_missionaries_on_right
    ncr = self.n_cannibals_on_right
    return (nmr+ncr==6)

  def __eq__(self, s2):
    if s2==None: return False
    if self.n_boats_on_right != s2.n_boats_on_right: return False
    if self.n_missionaries_on_right != s2.n_missionaries_on_right: return False
    if self.n_cannibals_on_right != s2.n_cannibals_on_right: return False
    return True

  def __str__(self):
    st = '('+str(self.n_missionaries_on_right)
    st += ','+str(self.n_cannibals_on_right)
    st += ','+str(self.n_boats_on_right)+')'
    return st

  def __hash__(self):
    return (str(self)).__hash__()

  def goal_message(self):
    return "Congratulations on successfully guiding the"+\
           " missionaries and cannibals across the river!"

def copy_state(s):
  return State(old=s)

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
phi0 = Operator("Cross the river with 1 missionary",
  lambda s: s.can_move(1,0),
  lambda s: s.move(1,0))

phi1 = Operator("Cross the river with 2 missionaries",
  lambda s: s.can_move(2,0),
  lambda s: s.move(2,0))

phi2 = Operator("Cross the river with 1 missionary and 1 cannibal",
  lambda s: s.can_move(1,1),
  lambda s: s.move(1,1))

phi3 = Operator("Cross the river with 2 missionaries and 1 cannibal",
  lambda s: s.can_move(2,1),
  lambda s: s.move(2,1))

phi4 = Operator("Cross the river with 3 missionaries",
  lambda s: s.can_move(3,0),
  lambda s: s.move(3,0))

OPERATORS = [phi0, phi1, phi2, phi3, phi4]
#</OPERATORS>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

#<STATE_VIS>

#</STATE_VIS>
