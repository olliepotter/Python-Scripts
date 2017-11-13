def c2f(celsius):
	f = 9 * celsius / 5 + 32
	return f

def f2c(fahrenheit):
	c = (5/9)*(fahrenheit-32)
	return c

temperature = input("Enter a temperature to convert to celsius = ")
cf = float(temperature)
celsius = f2c(cf)
print(celsius, "C")

print(c2f(celsius))