letters = "abcdefghijklmnopqrstuvwxyz"

backwards00 = letters[25:0:-1]  # start at index 25, up to but not including index 0, step backwards through string
backwards01 = letters[25::-1]  # start at index 25, up to the end of the string, step backwards through string
backwards02 = letters[::-1]  # start at the end of the string, up to the beginning of the string, step backwards through string
print(backwards00, backwards01, backwards02)

backwards03 = letters[16:13:-1]  # start at index 16, up to but not including index 13, step backwards through string
print(backwards03)

backwards04 = letters[4::-1]  # start at index 4, up to the end of the string, step backwards through string
print(backwards04)

backwards05 = letters[25:17:-1]  # start at index 25, up to but not including index 17, step backwards through string
backwards06 = letters[:-9:-1]  # start at the end of the string, up to but not including index -9, step backwards through string
print(backwards05)
print(backwards06)

print(letters[-4:])  # start at index -4, up to the end of the string -- Returns end of sequence.
print(letters[-1:])  # start at index -1, up to the end of the string -- Returns last item of sequence.
print(letters[:1])   # start at index 0, up to but not including index 1 -- Returns first item of sequence.
print(letters[0])    # start at index 0, including index 0  -- Returns first item of sequence.
