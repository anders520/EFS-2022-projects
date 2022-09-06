
#<METADATA>
SOLUZION_VERSION = "0.2"
PROBLEM_NAME = "Instant Insanity"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['A. Choy', 'D. Harris']
PROBLEM_CREATION_DATE = "31-AUG-2022"
PROBLEM_DESC =\
  '''This is Instant Insanity. It's insane. This game consists of four cubes with faces colored with four colors. 
  The objective of the puzzle is to stack these cubes in a column such that each side of the stack 
  (front, back, left, and right) has exactly one square in each of the four colors. The distribution of colors on each cube is unique. 
  And the cubes are randomly rotated.
  
  The numbers of the list represents the different colors: red = 0, blue = 1, green = 2, and yellow = 3
  The cube lists consist of 6 numbers, which represent the different sides of the cube [left, front, right, back, top, bottom]'''
#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>
import random as r

class State:
  def __init__(self, old=None):
    # Default new state is a state objects initialized as the
    # initial state.
    # If called with old equal to a non-empty state, then
    # the new instance is made to be a copy of that state.
    if not old is None:
      self.first_cube_list = old.first_cube_list
      self.second_cube_list = old.second_cube_list
      self.third_cube_list = old.third_cube_list
      self.fourth_cube_list = old.fourth_cube_list
    else:
      self.first_cube_list = [0, 0, 0, 1, 2, 3]
      self.second_cube_list = [1, 3, 1, 2, 0, 2]
      self.third_cube_list = [2, 1, 0, 3, 0, 3]
      self.fourth_cube_list = [2, 0, 3, 1, 1, 3]

  def can_move(self, boxNum, vertical, direction):
    # There are no restrictions in this game
    return True

  def move(self,boxNum, vertical, direction):
    news = State(old=self) # Make a copy of the current state.
    if boxNum == 1:
      boxes_list = news.first_cube_list
    elif boxNum == 2:
      boxes_list = news.second_cube_list
    elif boxNum == 3:
      boxes_list = news.third_cube_list
    elif boxNum == 4:
      boxes_list = news.fourth_cube_list
    
    if vertical == 0:
      if direction == 1: #right
        saved_box_element = boxes_list[3]
        for i in range(3):
          boxes_list[3 - i] = boxes_list[2 - i]
        boxes_list[0] = saved_box_element
      elif direction == 0: #left
        saved_box_element = boxes_list[0]
        for i in range(3):
          boxes_list[i] = boxes_list[i + 1]
        boxes_list[3] = saved_box_element
    elif vertical == 1:
      if direction == 1: #down
        saved_box_element = boxes_list[3]
        boxes_list[3] = boxes_list[5]
        boxes_list[5] = boxes_list[1]
        boxes_list[1] = boxes_list[4]
        boxes_list[4] = saved_box_element
      elif direction == 0: #up
        saved_box_element = boxes_list[4]
        boxes_list[4] = boxes_list[1]
        boxes_list[1] = boxes_list[5]
        boxes_list[5] = boxes_list[3]
        boxes_list[3] = saved_box_element
    elif vertical == 2:
      if direction == 1: #rotate clockwise
        saved_box_element = boxes_list[5]
        boxes_list[5] = boxes_list[2]
        boxes_list[2] = boxes_list[4]
        boxes_list[4] = boxes_list[0]
        boxes_list[0] = saved_box_element
      elif direction == 0: #rotate counter-clockwise
        saved_box_element = boxes_list[0]
        boxes_list[0] = boxes_list[4]
        boxes_list[4] = boxes_list[2]
        boxes_list[2] = boxes_list[5]
        boxes_list[5] = saved_box_element
    
    if boxNum == 1:
      news.first_cube_list = boxes_list
    elif boxNum == 2:
      news.second_cube_list = boxes_list
    elif boxNum == 3:
      news.third_cube_list = boxes_list
    elif boxNum == 4:
      news.fourth_cube_list = boxes_list

    return news

  def describe_state(self):
    # Produces a textual description of a state.
    # Might not be needed in normal operation with GUIs.
    l1 = self.first_cube_list
    l2 = self.second_cube_list
    l3 = self.third_cube_list
    l4 = self.fourth_cube_list
    txt = "First cube list: "+l1+"\n"
    txt += "Second cube list: "+l2+"\n"
    txt += "Third cube list: "+l3+"\n"
    txt += "Fourth cube list :"+l4+"\n"
    return txt

  def is_goal(self):
    correct_faces = 0
    for i in range(4):
      goal = (self.first_cube_list[i] != self.second_cube_list[i] and self.first_cube_list[i] != self.third_cube_list[i]\
        and self.first_cube_list[i] != self.fourth_cube_list[i] and self.second_cube_list[i] != self.third_cube_list[i]\
        and self.second_cube_list[i] != self.fourth_cube_list[i] and self.third_cube_list[i] != self.fourth_cube_list[i])
      if goal:
        correct_faces +=1
    return (correct_faces == 4)

  def __eq__(self, s2):
    if s2==None: return False
    if self.first_cube_list != s2.first_cube_list: return False
    if self.second_cube_list != s2.second_cube_list: return False
    if self.third_cube_list != s2.third_cube_list: return False
    if self.fourth_cube_list != s2.fourth_cube_list: return False
    return True

  def __str__(self):
    color_list1 = []
    for c1 in self.first_cube_list:
      if c1 == 0: color = 'red'
      elif c1 == 1: color = 'green'
      elif c1 == 2: color= 'blue'
      elif c1 == 3: color = 'yellow'
      color_list1.append(color)
    color_list2 = []
    for c2 in self.second_cube_list:
      if c2 == 0: color = 'red'
      elif c2 == 1: color = 'green'
      elif c2 == 2: color= 'blue'
      elif c2 == 3: color = 'yellow'
      color_list2.append(color)
    color_list3 = []
    for c3 in self.third_cube_list:
      if c3 == 0: color = 'red'
      elif c3 == 1: color = 'green'
      elif c3 == 2: color= 'blue'
      elif c3 == 3: color = 'yellow'
      color_list3.append(color)
    color_list4 = []
    for c4 in self.fourth_cube_list:
      if c4 == 0: color = 'red'
      elif c4 == 1: color = 'green'
      elif c4 == 2: color= 'blue'
      elif c4 == 3: color = 'yellow'
      color_list4.append(color)
    color_list = '('+str(color_list1)
    color_list += ','+str(color_list2)
    color_list += ','+str(color_list3)
    color_list += ','+str(color_list4)+')'
    st = '('+str(self.first_cube_list)
    st += ','+str(self.second_cube_list)
    st += ','+str(self.third_cube_list)
    st += ','+str(self.fourth_cube_list)+')'
    return color_list

  def __hash__(self):
    return (str(self)).__hash__()

  def goal_message(self):
    return "Congratulations on successfully solving Instant Insanity!"

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

#<OPERATORS>
phi0 = Operator("Rotate 1st cube left",
  lambda s: s.can_move(1, 0, 0),
  lambda s: s.move(1, 0, 0))

phi1 = Operator("Rotate 1st cube right",
  lambda s: s.can_move(1, 0, 1),
  lambda s: s.move(1, 0, 1))

phi2 = Operator("Rotate 1st cube up",
  lambda s: s.can_move(1, 1, 0),
  lambda s: s.move(1, 1, 0))

phi3 = Operator("Rotate 1st cube down",
  lambda s: s.can_move(1, 1, 1),
  lambda s: s.move(1, 1, 1))

phi4 = Operator("Rotate 1st cube counter-clockwise",
  lambda s: s.can_move(1, 2, 0),
  lambda s: s.move(1, 2, 0))

phi5 = Operator("Rotate 1st cube clockwise",
  lambda s: s.can_move(1, 2, 1),
  lambda s: s.move(1, 2, 1))

phi6 = Operator("Rotate 2nd cube left",
  lambda s: s.can_move(2, 0, 0),
  lambda s: s.move(2, 0, 0))
  
phi7 = Operator("Rotate 2nd cube right",
  lambda s: s.can_move(2, 0, 1),
  lambda s: s.move(2, 0, 1))

phi8 = Operator("Rotate 2nd cube up",
  lambda s: s.can_move(2, 1, 0),
  lambda s: s.move(2, 1, 0))

phi9 = Operator("Rotate 2nd cube down",
  lambda s: s.can_move(2, 1, 1),
  lambda s: s.move(2, 1, 1))

phi10 = Operator("Rotate 2nd cube counter-clockwise",
  lambda s: s.can_move(2, 2, 0),
  lambda s: s.move(2, 2, 0))

phi11 = Operator("Rotate 2nd cube clockwise",
  lambda s: s.can_move(2, 2, 1),
  lambda s: s.move(2, 2, 1))

phi12 = Operator("Rotate 3rd cube left",
  lambda s: s.can_move(3, 0, 0),
  lambda s: s.move(3, 0, 0))

phi13 = Operator("Rotate 3rd cube right",
  lambda s: s.can_move(3, 0, 1),
  lambda s: s.move(3, 0, 1))

phi14 = Operator("Rotate 3rd cube up",
  lambda s: s.can_move(3, 1, 0),
  lambda s: s.move(3, 1, 0))

phi15 = Operator("Rotate 3rd cube down",
  lambda s: s.can_move(3, 1, 1),
  lambda s: s.move(3, 1, 1))

phi16 = Operator("Rotate 3rd cube counter-clockwise",
  lambda s: s.can_move(3, 2, 0),
  lambda s: s.move(3, 2, 0))

phi17 = Operator("Rotate 3rd cube clockwise",
  lambda s: s.can_move(3, 2, 1),
  lambda s: s.move(3, 2, 1))

phi18 = Operator("Rotate 4th cube left",
  lambda s: s.can_move(4, 0, 0),
  lambda s: s.move(4, 0, 0))

phi19 = Operator("Rotate 4th cube right",
  lambda s: s.can_move(4, 0, 1),
  lambda s: s.move(4, 0, 1))

phi20 = Operator("Rotate 4th cube up",
  lambda s: s.can_move(4, 1, 0),
  lambda s: s.move(4, 1, 0))

phi21 = Operator("Rotate 4th cube down",
  lambda s: s.can_move(4, 1, 1),
  lambda s: s.move(4, 1, 1))

phi22 = Operator("Rotate 4th cube counter-clockwise",
  lambda s: s.can_move(4, 2, 0),
  lambda s: s.move(4, 2, 0))

phi23 = Operator("Rotate 4th cube clockwise",
  lambda s: s.can_move(4, 2, 1),
  lambda s: s.move(4, 2, 1))

OPERATORS = [phi0, phi1, phi2, phi3, phi4, phi5, phi6, phi7, phi8, phi9, phi10, phi11, phi12, phi13, phi14, phi15, phi16, phi17, phi18, phi19, phi20, phi21, phi22, phi23]
#</OPERATORS>

#<INITIAL_STATE>
INITIAL_STATE = State()
randomize_times = r.randint(5, 100)
for i in range(randomize_times):
  move_num = r.randint(0,23)
  INITIAL_STATE = OPERATORS[move_num].apply(INITIAL_STATE)
#</INITIAL_STATE>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

#<STATE_VIS>

#</STATE_VIS>
