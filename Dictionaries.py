# Dictionaries are used to store data in key:value pairs
# A dictionary is ordered (Python 3.7+), changeable, and does not allow duplicate keys

# Creating a dictionary
thisdict = {
    "brand": "Ford",     # key = brand, value = Ford
    "model": "Mustang",  # key = model, value = Mustang
    "year": 1964         # key = year, value = 1964
}

# Print the entire dictionary
print(thisdict)

# Accessing items using key
x = thisdict["model"]   # gets the value of key "model"
print(x)

# Changing a value
thisdict["year"] = 2018   # update year from 1964 to 2018
print(thisdict)

# Looping through dictionary (keys only)
for x in thisdict:
    print(x)   # prints keys (brand, model, year)

# Looping through dictionary (values using keys)
for x in thisdict:
    print(thisdict[x])   # prints values

# Looping through values directly
for x in thisdict.values():
    print(x)

# Looping through both keys and values
for x, y in thisdict.items():
    print(x, y)   # prints key and value pair


# Dictionary for month conversions (short form → full name)
mothConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# Access value using key
print(mothConversions["Nov"])   # direct access

# Using get() method (safer than [])
print(mothConversions.get("Dec"))   # returns "December"

# If key does not exist → returns None
print(mothConversions.get("vuv"))

# Providing default value if key is not found
print(mothConversions.get("vuv", "Not a valid key"))