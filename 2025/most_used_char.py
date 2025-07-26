string = "abcdavkhlahgacldadanavhkidsacdadhakja;acakj===="
list = []
for char in string:
    list.append(char)
print(list)
print(len(list))
print(max(list))
most_repeated = max(list, key=list.count)
count = list.count(most_repeated)
print(f"The most repeated item is {most_repeated} and {count} times repeated")
print(f"{most_repeated}: {count}")