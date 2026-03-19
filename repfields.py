# String formatting using the .format() method with indexed placeholders
# The format() method allows positional arguments to be referenced by index number

# Simple example with one format argument
age = 24
# Commented example showing old-style string concatenation with type coercion
#print("My age is " + str(age) + " years")   # use str function to coerce int into str
# Modern approach using .format() method:
print("My age is {0} years".format(age))  # use format method to insert age into string
# {0} refers to the first argument passed to format()

# Multiple distinct arguments - each placeholder refers to a unique argument position
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
# {0}="31", {1}="Jan", {2}="Mar", {3}="May", {4}="Jul", {5}="Aug", {6}="Oct", {7}="Dec"

# Reusing the same argument - {0} can be referenced multiple times
print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct, Dec".format(31))
# {0} is used only once and refers to the value 31

# Reordered and reused arguments - demonstrating that indices can appear in any order
# Days in Feb=28, Apr/Jun/Sep/Nov=30, Jan/Mar/May/Jul/Aug/Oct/Dec=31
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))
# {0}=28 (February days), {1}=30 (30-day months), {2}=31 (31-day months)
# Notice {2} and {1} are used multiple times throughout the string

print()

# Multi-line string formatting using triple-quoted strings
# This demonstrates the same format arguments but displayed across multiple lines
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}
""".format(28, 30, 31))
# Triple quotes (""") allow strings to span multiple lines while preserving newline characters
# The format() method is called on the entire multi-line string at the end
