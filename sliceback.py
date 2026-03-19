# Reverse slicing demonstrations - extracting substrings in reverse order using negative step values
# String of lowercase letters for slicing examples
##         0         1         2
## Index:  01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

# Reverse slicing with explicit start and stop indices
# [start:stop:step] with step=-1 reverses the string within the specified range
backwards00 = letters[25:0:-1]  # start at index 25 (z), up to but NOT including index 0, step backwards by 1
# Result: "zyxwvutsrqponmlkjihgfedcb" (all except 'a')

backwards01 = letters[25::-1]  # start at index 25 (z), go to beginning of string, step backwards by 1
# Result: "zyxwvutsrqponmlkjihgfedcba" (entire string reversed)

backwards02 = letters[::-1]  # start at end of string, go to beginning of string, step backwards by 1
# Result: "zyxwvutsrqponmlkjihgfedcba" (entire string reversed, same as above)

# All three print their results separated by spaces
print(backwards00, backwards01, backwards02)

# Reverse slicing of a small substring in the middle of the string
backwards03 = letters[16:13:-1]  # start at index 16 (q), up to but NOT including index 13 (n), step backwards by 1
# Result: "qpo" (indices 16, 15, 14)
print(backwards03)

# Reverse slicing from a middle position to the beginning
backwards04 = letters[4::-1]  # start at index 4 (e), go to beginning of string, step backwards by 1
# Result: "edcba" (from index 4 down to index 0, inclusive)
print(backwards04)

# Reverse slicing with different stop points
backwards05 = letters[25:17:-1]  # start at index 25 (z), up to but NOT including index 17 (r), step backwards by 1
# Result: "zyxwvuts" (indices 25, 24, 23, 22, 21, 20, 19, 18)
backwards06 = letters[:-9:-1]  # start at end of string, up to but NOT including index -9 (r), step backwards by 1
# Negative index -9 is equivalent to index 17 (26 - 9 = 17)
# Result: "zyxwvuts" (same as backwards05, demonstrates negative indexing with negative step)
print(backwards05)
print(backwards06)

# Practical slicing examples: retrieving end and beginning characters
print(letters[-4:])  # start at index -4 (w), go to end of string - Returns last 4 characters: "wxyz"
# Negative indices count from the end: -1 is 'z', -2 is 'y', -3 is 'x', -4 is 'w'

print(letters[-1:])  # start at index -1 (z), go to end of string - Returns last 1 character: "z"
# Even though -1 is the last character, slicing with -1: returns a string (not a character)

print(letters[:1])   # start at index 0, up to but NOT including index 1 - Returns first character: "a"
# Slicing returns a string, even if it's just one character

print(letters[0])    # Direct indexing at index 0 - Returns first character: "a"
# Direct indexing returns a single character (string of length 1)
