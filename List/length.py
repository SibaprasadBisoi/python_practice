list = [1, 2, 4, 5, 6, 1, 5, 78, 98, 100]
print(len(list))
#Using iterator
count = 0
for i in list:
    count += 1
print(count)

#Length_hint
from operator import length_hint
print(length_hint(list))

#Lambda
print(sum(1 for i in list))

#List comprehension
print(sum(1 for _ in list))

#Using recursion
def count_elements_recursion(list):
    if not list:
        return 0
    return 1 + count_elements_recursion(list[1:])
print(count_elements_recursion(list))