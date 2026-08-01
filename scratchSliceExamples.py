# String slicing demonstrations with various start:stop:step combinations
#                 1         2         3
#       01234567890123456789012345678901234567
data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"

# Full string slice - equivalent to data[0:len(data):1] or just data
print(data[::])  # "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H" - entire string

# Slice from start to second-to-last character (excluding the last character)
print(data[0:-1])  # "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:" - all except last character 'H'

# Every 5th character starting from index 0
print(data[0::5])  # "12345678" - characters at positions 0,5,10,15,20,25,30,35

# Same as above - every 5th character starting from index 0 (default start is 0)
print(data[::5])  # "12345678" - same result as data[0::5]

# Every 5th character from start to second-to-last character
print(data[0:-1:5])  # "12345678" - same as above since -1 doesn't affect the step pattern

# Same as above - every 5th character from start to second-to-last
print(data[:-1:5])  # "12345678" - equivalent to data[0:-1:5]

# Basic slice - characters from index 1 to 4 (up to but not including index 5)
print(data[1:5])  # ":A, " - characters at positions 1,2,3,4
