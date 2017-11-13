def c2f(celsius):
	f = 9 * celsius / 5 + 32
	return f

temperature = input("Enter a temperature to convert to fahrenheit = ")
ff = float(temperature)
fahrenheit = c2f(ff)
print(fahrenheit, "F")