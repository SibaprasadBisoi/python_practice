list = [2, 4, 6, 7]
list.append(9)
print(list)
print(list.sort())
list.append(1)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
print(list.index(1))
print(list.count(1))
m = list.copy()
print(m[3])
m.insert(1, 777)
print(m)
list.extend(m)
print(list)
print(list.count(1))