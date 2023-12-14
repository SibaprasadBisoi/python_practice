def swaplist(list):
    list[0],list[-1] = list[-1],list[0]
    return list
list = [1, 2, 3, 4, 5]
print(swaplist(list))

def swaplist2(list2):
    size = len(list2)

    temp = list2[0]
    list2[0] = list2[size -1]
    list2[size -1] = temp
    return list2
list2 = ["siba", "prasad", "bisoi", "budu", "bisoi"]
print(swaplist2(list2))
