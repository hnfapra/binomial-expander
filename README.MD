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
