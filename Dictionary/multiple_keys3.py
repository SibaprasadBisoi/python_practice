# Creating a dictionary with multiple inputs for keys
data = {
    (1, "John", "Doe"): {"a": "geeks", "b": "software", "c": 75000},
    (2, "Jane", "Smith"): {"e": 30, "f": "for", "g": 90000},
    (3, "Bob", "Johnson"): {"h": 35, "i": "project", "j": "geeks"},
    (4, "Alice", "Lee"): {"k": 40, "l": "marketing", "m": 100000}
}

print(data)
print("\n")
print(data[(1, "John", "Doe")]["b"])
print(data[(3, "Bob", "Johnson")]['i'])
mykeys =[]
keys = data.keys()
for i in keys:
    mykeys.append(i)
print(mykeys[3])