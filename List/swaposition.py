def swaplist(list):
    size = len(list)

    temp = list[0]
    list[0] = list[size - 1]
    list[size-1] = temp

    return list
newlist = [1, 2, 3, 4]
print(swaplist(newlist))