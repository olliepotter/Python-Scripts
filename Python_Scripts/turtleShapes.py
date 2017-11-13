from exturtle import *

def polygon(t, n=3, length=200, colour = "blue", width = 1):
	color(t, colour)
	pensize(t, width)
	for i in range(n):
		forward(t, length)
		right(t, (360/n))
		
	return n*length
		
myTurtle = Turtle()	

print(polygon(myTurtle))
print(polygon(myTurtle, 8, 50, "red", 5))
