import math

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def square(x):
    return x ** 2

def mod(x, y):
    return x % y

def distance(x1, y1, x2, y2):
    return math.sqrt(square(x2 - x1) + square(y2 - y1))
