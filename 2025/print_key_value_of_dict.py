string = "abcdavkhlahgacldadanavhkidsacdadhakja;acakj===="
list= []
for char in string:
    list.append(char)
dict = {}
for i in list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for key, value in dict.items():
    print(f'{key}: {value}')