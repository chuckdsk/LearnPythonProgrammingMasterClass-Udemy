string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5) # he's probably pining for the fjords

print("he's " "probably " "pining " "for the " "fjords") # he's probably pining for the fjords

print("Hello " * 5) # Hello Hello Hello Hello Hello

#print("Hello " * 5 + 4) # TypeError: can only concatenate str (not "int") to str

print("Hello " * (5 + 4)) # Hello Hello Hello Hello Hello Hello Hello Hello Hello
print("Hello " * 5 + "4") # Hello Hello Hello Hello Hello 4

today = "friday"
print("day" in today) # True
print("fri" in today) # True
print("thur" in today) # False
print("parrot" in "fjord") # False
