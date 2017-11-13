from math import sqrt

def circumcircle(a, b, c):
	s = (a + b + c) / 2
	d = (a*b*c) / (2 * sqrt(s*(s-a)*(s-b)*(s-c)))
	return d / 2
	
print(circumcircle(6, 4, 3))
print(circumcircle(10, 25, 30))
print(circumcircle(3, 4, 5)) 