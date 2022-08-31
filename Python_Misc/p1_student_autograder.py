import achoy06_p1 as student

'''
This file is the student autograder program for
Project 1 in CSE 190C, Early Fall Start, 2022.

It can help to debug a solution to the assignment
by providing partial feedback.  Note that the
tests in this autograder are not "comprehensive."
So passing all the tests here, although very
important to do, does not guarantee that all your
functions are completely correct.  The instructor
will use a separate autograder to test even more
cases for these functions, after you have 
submitted your assignment.


'''

print("Student autograder report for "+student.FIRST_NAME+" "+student.LAST_NAME)
if student.OPTIONAL_PARTNER_FIRST_NAME != "(none)":
  print("  in partnership with", student.OPTIONAL_PARTNER_FIRST_NAME,\
                               student.OPTIONAL_PARTNER_LAST_NAME)
POINTS = 0

def test1(ex_no, fn, arg1, correct_answer, points):
  global POINTS
  try:
     st_answer = fn(arg1)
     if st_answer==correct_answer:
       POINTS += points
       print("Correct. For input, "+str(arg1)+", output is "+str(st_answer))
     else:
       print("In Exercise "+str(ex_no)+", the result was not correct.")
       print("For the input, "+str(arg1)+", the output should be, "+str(correct_answer))
       print("Your function returned: "+str(st_answer))
  except Exception as e:
    print("An exception was raised, while testing this exercise.")
    print(e)
  print() 

print("EXERCISE 1:")
test1(1, student.triple, 5, 15, 1)

print("EXERCISE 2:")
test1(2, student.four_x_squared_plus_seven_x_plus_two, 5, 137, 2)

print("EXERCISE 3:")
test1(3, student.please_repeat_that, "Let's have fun.", "Let's have fun. -- I said, Let's have fun.", 2)

print("EXERCISE 4:")
# EXERCISE 4:

die_result = student.roll_die()
if die_result in [1,2,3,4,5,6]:
  print("roll_die worked. The result was "+str(die_result))
  POINTS += 2
else:
  print("roll_die did not work.")
  print("It did not return one of the numbers 1, 2, 3, 4, 5, or 6.")
print()

print("EXERCISE 5:")
# EXERCISE 5:
test1(5, student.twelfth_root, 4096, 2.0, 2)

print("EXERCISE 6:")
# EXERCISE 6:
test1(6, student.makepal, [1, 5], [1, 5, 5, 1], 1)
test1(6, student.makepal, 'Hello Echo', 'Hello EchoohcE olleH', 1)

print("EXERCISE 7:")
# EXERCISE 7:
try:
  jane_eyre = student.Movie('romance', 'Jane Eyre', 'Stevenson',\
       '1943', 'English', ['Orson Wells','Joan Fontaine'], \
       'After a harsh childhood, orphan Jane Eyre is hired '+\
       'by Edward Rochester, the brooding lord of a mysterious '+\
       'manor house, to care for his young daughter.')
  print("Instantiation of the Movie class succeeded.")
  POINTS += 2
except Exception as e:
  print("An exception was raised, while testing the Movie class.")
  print(e)
print()

try:
  romance_movies = student.by_genre([jane_eyre], 'romance')
  horror_movies = student.by_genre([jane_eyre], 'horror')
  if romance_movies[0]==jane_eyre:
     print("First test of by_genre passes.")
     POINTS += 2
  else:
     print("First test of by_genre fails.")
  if horror_movies==[]:
     print("Second test of by_genre passes.")
     POINTS += 2
  else:
     print("Second test of by_genre fails.")
except Exception as e:
  print("An exception was raised, while testing the by_genre function.")
  print(e)
print()

print("EXERCISE 8:")
# EXERCISE 8:

print("Let's test is_prime:")
test1(8, student.is_prime, 2, True, 1)
test1(8, student.is_prime, 29, True, 1)
test1(8, student.is_prime, 33, False, 1)

print("Let's test does_p_divide_n_minus_m")
fn1 = lambda p: student.does_p_divide_n_minus_m(p, 15, 1)
print("First, with p=7, n=15, m=1")
test1(8, fn1, 7, True, 1)
print("Next, with p=2, n=15, m=1")
test1(8, fn1, 2, True, 1)
print("Next, with p=3, n=15, m=1")
test1(8, fn1, 3, False, 1)
print("Next, with p=5, n=15, m=1")
test1(8, fn1, 5, False, 1)

print("Your score will be at least "+str(POINTS))
print("The actual number of possible points will depend on additional testing by the instructor, after submission of your file.")
