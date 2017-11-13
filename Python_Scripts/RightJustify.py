def right_justify(string, width):
	length = width - len(string)
	print(" "*length + string)
	
	
	
right_justify("Hello", 50)

w = 50
right_justify("The owl and the pussycat", width=w)
right_justify("In a beautiful pea-green boat,", width=w)
right_justify("They took some honey, and plenty of money,", width=w)
right_justify("Wrapped up in a five pound note.", width=w)	