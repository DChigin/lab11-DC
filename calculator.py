#https://github.com/DChigin/lab11-DC
import math

def square_root(a):
	try:
		return math.sqrt(a)
	except ValueError:
		raise ValueError("Cannot take square root of a negative number.")

def hypotenuse(a,b):
	return math.hypot(a,b)

def add(a, b): 
	return a + b

def subtract(a, b): 
	return a - b

def mul(a, b): 
	return a * b

def div(a, b): 
	if a==0:
		raise ZeroDivisionError("Cannot be divided by zero!")
	return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Log base 'a' must be positive and not 1.")
    if b <= 0:
        raise ValueError("Log argument 'b' must be positive.")
    return math.log(b, a)

def exp(a, b): 
	return a**b






