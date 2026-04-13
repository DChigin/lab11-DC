"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
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

def multiply(a, b): 
	return a * b

def divide(a, b): 
	if a==0:
		raise ZeroDivisionError("Cannot be divided by zero!")
	return b / a

def logarithm(a, b): 
	if a<= 0 or a==1:
		raise ValueError("Log base must be greater than 0 but not equal to 1")
	if b<=0:
		raise ValueError("Log argument must be greater than 0")

def exponent(a, b): 
	return a**b






