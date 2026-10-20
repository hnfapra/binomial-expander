# Binomial Expansion Calculator

This is A Python based calculator that computes coefficient and displays the expanded form using fraction. 

The calculator works with expression of the form 

$(1+kx)^n$

After getting the input, it calculates each coefficient of the terms using the recurrence relation

$c_{r+1}=c_r\frac{n-r}{r+1}k$

where $c_0=1$

Requirements: 
- Python 3
- Rich


## Installation
Install the package directly from PyPI using pip:

    python -m pip install binomial-expander

## Usage
After installation, launch the calculator with:

    binomial-calculator

Follow the prompts in the terminal:
1. Terms, enter the number of terms you want to display.
2. Coefficient (k), enter the coefficient of x.
3. Power (n), enter the exponent of the binomial expression

## Example
As an example we use this binomial expression

$(1+2x)^{3}$

Enter the following values

    term > 4
    k > 2
    n > 3

Expected mathematical result:

$ (1+2x)^3 = 1 + 6x + 12x^2 + 8x^3$

The terminal interface will present the expanded expression in a formatted panel.
