import fractions
from math import fsum
import random as rand

# Import the fractions module and create a Fraction from the float 2.25
f = fractions.Fraction(2.25)
print(f) #9/4

# Import only the fsum function from the math module and use it to find
# the sum of the following series of floats:
numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]
s = fsum(numbers)
print(s) #118.482

# Import the random module using an alias, and find a random number between
#  1 and 100 using the randint function.
x = rand.randint(1, 100)
print(x)