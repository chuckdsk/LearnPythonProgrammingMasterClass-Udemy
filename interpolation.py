# String interpolation using the % operator (old-style formatting, predates .format() and f-strings)
# This is an alternative to .format() and f-strings for inserting values into strings

# Integer variable assignment
age = 24

# % operator interpolation with %d (decimal/integer) format specifier
# %d - placeholder for an integer value
# % age - replaces %d with the value of the age variable
print("My age is %d years" % age)

# String variables for use in multi-value interpolation
major = "years"
minor = "months"

# Multi-value interpolation using multiple format specifiers
# %d - first placeholder (age), expects an integer
# %s - second placeholder (major), expects a string
# %d - third placeholder (6), expects an integer
# %s - fourth placeholder (minor), expects a string
# The % operator takes a tuple of values that fill the placeholders in order
print("My age is %d %s, %d %s" % (age, major, 6, minor))

# %f format specifier for floating-point numbers (default precision is 6 decimal places)
# %f - placeholder for a float value
# 22 / 7 - calculates the approximation of Pi
print("Pi is approximately %f" % (22 / 7))

# %60.50f - width and precision specification for floating-point numbers
# 60 - minimum field width (total characters, right-aligned by default)
# .50 - precision (50 decimal places)
# f - floating-point format specifier
print("Pi is approximately %60.50f" % (22 / 7))
