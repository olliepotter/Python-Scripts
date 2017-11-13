#  Simple test and demonstration of the exturtle code.

from exturtle import *          # Import all the exturtle functions 

fred = Turtle()                 # Create a turtle.  
# The Turtle() function should create a new window with an
# arrow indicating the position and heading of your turtle 'fred'

forward(fred, 100)              # Move fred forward by 100 units
left(fred, 45)                  # Turn left 45 degrees
forward(fred, 200)              # Foward by another 200 units
right(fred, 90)                 # Turn right 90 degrees
backward(fred, 60)              # Backwards by 60 units

# The following function keeps the current drawing on screen 
# until you close the window; if it were not here the picture
# would disappear too quickly for you to see.
# Code after this will not be executed
# until the window is closed, so usually this will be the 
# last statement in your program.

mainloop()                    
