"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
#defining the dictionary
personal = {
  "name": "anvesh",
  "mobile": '000000000',
  "email": "test@gmail.com"
}

#printing the dictionary
print(personal)
#printing the single value from dictionary
print(personal["name"])
#printing the size of the dictionary
print(len(personal))

#defining the dictionary values with array
personal2 = {
  "name": "anvesh",
  "mobile": '000000000',
  "interests": ["K8'S","Python"]
}
#printing the dictionary
print(personal2)
#printing the single value from the dictionary
print(personal2["interests"])
#Printing the type i.e. dictionary
print(type(personal2))
#printing the type i.e. list
print(type(personal2["interests"]))