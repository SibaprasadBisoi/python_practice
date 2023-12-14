def swaposition(list, pos1, pos2):
    list[pos1], list[pos2]  = list[pos2], list[pos1]
    return list
list = [1, 3, 5, 7, 9]
pos1, pos2 =1, 3
print(swaposition(list, pos1, pos2))