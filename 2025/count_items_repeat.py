list = ["audi", "bmw", "Benz", "bmw", "Mg", "Benz"]
dict = {}
for item in list:
    if  item in dict:
        dict[item]  += 1
    else:
        dict[item] = 1
print(dict)
max_count = max(dict.values())
max_key = max(dict, key=dict.get)
print(f"The most repeated car is {max_key} and {max_count} times")
most_repeated = [k for k, v in dict.items() if v == max_count]
print(most_repeated)