# playing with strings
string = 'example' 
string_arr = [c for c in string]
string_arr.sort()
string_arr.reverse()
string = ''
for c in string_arr:
    string += c
print(string)

# Returning the max and min
string = 'example'
min_char = 'z'
max_char = 'a'
for char in string:
    if char < min_char:
        min_char = char
    if char > max_char:
        max_char = char
print(min_char, max_char)
print(min(string), max(string))

# mins and maxes
print(min('example')) # a
print(min(['e', 'x', 'a', 'm', 'p', 'l', 'e'])) # a