string = "this is a test string and this string is used or finding the most repeated word in string"
list = string.split(" ")
most_repeated = max(list, key=list.count)
count = list.count(most_repeated)
print(f"{most_repeated}: {count}")