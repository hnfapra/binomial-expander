import math
from fractions import Fraction

def expand (n, term, b):
    r = 0
    coefficient = 1.0
    coefficients = [coefficient]
    
    for i in range(term):
        coefficient *= (n-r)/(r+1)*b
        coefficients.append(coefficient)
        r = r + 1
        

def convertfrac (decimals):
    for number in decimals:
        answers = []
        frac = Fraction(number).limit_denominator()
        stringres = f"{frac.numerator}/{frac.denominator}"
        answers.append(stringres)
        # print(f"{result.numerator}/{result.denominator}")
        