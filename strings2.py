#                   1
#         012345678901234
parrot = "Norwegian Blue"

# slicing - extracting parts of a string using the slice operator [start:stop:step]
print(parrot[0:6:2])  # Nre - start at index 0, up to but not including index 6, step by 2
print(parrot[0:6:3])  # Nw - start at index 0, up to but not including index 6, step by 3

number = "9,223;372:036 854,775;807"
#print(number[1::4])  # ,,,,, - start at index 1, up to the end of the string, step by 4
seperators = number[1::4]  # ,,,,, - start at index 1, up to the end of the string, step by 4
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split() # replace each seperator with
# a space, then split the string into a list of values

print([int(val) for val in values])  # [9, 223, 372, 36, 854, 775, 807] -
# convert each value in values to an integer and print as a list

#print(parrot[0:6])  # Norweg - start at index 0, up to but not including index 6

# negative indexing - counting from end of string
#print(parrot[-14:-8])  # Norweg - start at index -14, up to but not including index -8
#print(parrot[-4:2])  # Nothing printed - start at index -4, up to but not including index 2 -
                     # can't go backwards from starting position
#print(parrot[-4:-2])  # Bl - start at index -4, up to but not including index -2
#print(parrot[-4:12])  # Bl - start at index -4, up to but not including index 12


#print(parrot[3:5])  # we - start at index 3, up to but not including index 5
#print(parrot[0:9])  # Norwegian - start at index 0, up to but not including index 9
#print(parrot[:9])  # Norwegian - start at index 0, up to but not including index 9

#print(parrot[10:14])  # Blue - start at index 10, up to but not including index 14
#print(parrot[10:])  # Blue - start at index 10, up to the end of the string

#print(parrot[:6])  # Norweg - start at index 0, up to but not including index 6
#print(parrot[6:])  # ian Blue - start at index 6, up to the end of the string

#print(parrot[:6] + parrot[6:])  # Norweg + ian Blue = Norwegian Blue

#print(parrot[:])  # Norwegian Blue - start at index 0, up to the end of the string

#                     1         2
#           01234567890123456789012345
#letters = "abcdefghijklmnopqrstuvwxyz"

#print(parrot[0:14])  # Norwegian Blue - start at index 0, up to but not including index 14
#print(parrot[:6])  # Norweg - start at index 0, up to but not including index 6
#print(parrot[3:])  # wegian Blue - start at index 3, up to the end of the string

#print(parrot)

#print(parrot[3])
#print(parrot[4])
#print(parrot[9])
#print(parrot[3])
#print(parrot[6])
#print(parrot[8])

#print()

#print(parrot[-11])
#print(parrot[-10])
#print(parrot[-5])
#print(parrot[-11])
#print(parrot[-8])
#print(parrot[-6])

#print()

#print(parrot[3 - 14])
#print(parrot[4 - 14])
#print(parrot[9 - 14])
#print(parrot[3 - 14])
#print(parrot[6 - 14])
#print(parrot[8 - 14])
