def sum_of_dictionary(dictionary):
    list =[]
    for i in dict:
        list.append(dict[i])
        final = sum(list)
        return final
dict = {'a': 400, 'b': 600, 
        'c': 1000}
print(sum_of_dictionary(dict))