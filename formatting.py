# Loop from 1 to 12 to demonstrate string formatting with field widths
for i in range(1, 13):
    # Format string with numbered fields and width specifications:
    # {0:2} - first argument (i), minimum width 2
    # {1:3} - second argument (i**2), minimum width 3
    # {2:4} - third argument (i**3), minimum width 4
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i **3))

print()

# Loop from 1 to 12 with left-aligned formatting
for i in range(1, 13):
    # Format string with left-aligned fields (< specifier):
    # {0:2} - first argument (i), minimum width 2, default right-aligned
    # {1:<3} - second argument (i**2), minimum width 3, left-aligned
    # {2:<4} - third argument (i**3), minimum width 4, left-aligned
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i **3))

print()

# Loop from 1 to 12 with center-aligned formatting
for i in range(1, 13):
    # Format string with mixed alignment specifiers:
    # {0:2} - first argument (i), minimum width 2, default right-aligned
    # {1:<3} - second argument (i**2), minimum width 3, left-aligned
    # {2:^4} - third argument (i**3), minimum width 4, center-aligned (^ specifier)
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i**2, i **3))

print()

# Demonstrating floating-point formatting with different width and precision specifications
# {0:12} - width 12, default representation (converts to float)
print("Pi is approximately {0:12}".format(22 / 7))

# {0:12f} - width 12, floating-point format (f specifier), default precision 6 decimal places
print("Pi is approximately {0:12f}".format(22 / 7))

# {0:12.50f} - width 12, floating-point format, 50 decimal places precision
print("Pi is approximately {0:12.50f}".format(22 / 7))

# {0:52.50f} - width 52 (adds padding), floating-point format, 50 decimal places precision
print("Pi is approximately {0:52.50f}".format(22 / 7))

# {0:62.50f} - width 62 (more padding), floating-point format, 50 decimal places precision
print("Pi is approximately {0:62.50f}".format(22 / 7))

# {0:72.50f} - width 72 (even more padding), floating-point format, 50 decimal places precision
print("Pi is approximately {0:<72.50f}".format(22 / 7))

# {0:<72.54f} - width 72, left-aligned (< specifier), floating-point format, 54 decimal places precision
# Demonstrates how left-alignment differs from right-alignment when padding is applied
print("Pi is approximately {0:<72.54f}".format(22 / 7))

print()

# Loop from 1 to 12 demonstrating implicit positional arguments
# This is a simpler syntax compared to the numbered fields above
for i in range(1, 13):
    # Format string with empty braces {} - arguments are filled in order (0, 1, 2, ...)
    # {} - first placeholder (i)
    # {} - second placeholder (i**2)
    # {} - third placeholder (i**3)
    # No explicit numbering needed; the format() method fills them sequentially
    print("No. {} squared is {} and cubed is {}".format(i, i**2, i **3))

print()

# Loop from 1 to 12 demonstrating implicit positional arguments with field width
for i in range(1, 13):
    # Format string with empty braces {} and one explicit width specification:
    # {} - first placeholder (i), no width specified
    # {} - second placeholder (i**2), no width specified  
    # {:4} - third placeholder (i**3), minimum width 4 (right-aligned by default)
    # Shows how to mix implicit arguments with specific formatting for individual fields
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i **3))
