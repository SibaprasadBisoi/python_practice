list = [12, 56, 89, 545, 85]
even, odd = 0, 0
for num in list:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("even numbers in the list: ", even)
print("odd numbers in the list: ", odd)


# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]
 
odd_count = len(list(filter(lambda x: (x%2 != 0) , list1)))
 
# we can also do len(list1) - odd_count
even_count = len(list(filter(lambda x: (x%2 == 0) , list1)))
 
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
