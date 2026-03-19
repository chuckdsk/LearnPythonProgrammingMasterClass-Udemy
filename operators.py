# Arithmetic operators demonstration in Python
# This file shows basic mathematical operations and operator precedence

# Variable assignment - storing values in variables for reuse
a = 12
b = 3

# Basic arithmetic operators
print(a + b)    # 15 - Addition operator (+)
print(a - b)    # 9 - Subtraction operator (-)
print(a * b)    # 36 - Multiplication operator (*)
print(a / b)    # 4.0 - Division operator (/), always returns float in Python 3
print(a // b)   # 4 integer division, rounded down towards minus infinity
print(a % b)    # 0 modulo: he remainder after integer division

print()

# Complex expressions demonstrating operator precedence
# Python follows PEMDAS/BODMAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
print(a + b / 3 - 4 * 12)  # Without explicit parentheses - division and multiplication happen first

# Same expression with explicit parentheses to show evaluation order
print(a + (b / 3) - (4 * 12))  # Parentheses make the order explicit

# Commented step-by-step evaluation of the expression:
# print(12 + (3 / 3) - (4 * 12))  # Step 1: 3/3=1, 4*12=48
# print(12 + 1 - 48)             # Step 2: 12+1=13, then 13-48
# print(-35)                      # Step 3: Final result

# More complex nested parentheses examples
# Extra parentheses for clarity, though not strictly necessary
print ((((a + b) / 3) - 4) * 12)  # Multiple levels of parentheses

# Same calculation with fewer parentheses - Python evaluates left to right with precedence
print (((a + b) / 3 - 4) * 12)    # Equivalent to above, but more concise

# Breaking down the calculation into steps using intermediate variables
c = a + b   # 15 - First add a and b
d = c / 3   # 5.0 - Then divide by 3
e = d - 4   # 1.0 - Subtract 4 (note: comment was incomplete in original)
print(e * 12)  # 12.0 - Finally multiply by 12

print()

# Complex division example showing left-to-right evaluation
# Parentheses show the actual evaluation order
print(a / (b * a) / b)  # 12 / (3 * 12) / 3 = 12 / 36 / 3 = 0.1111111111111111
