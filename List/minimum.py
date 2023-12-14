def mini(a, b):

    if a <= b:
        return a
    else:
        return b
a, b = 87, 99
print(mini(a, b))
print(min(a, b))
print(a if a<=b else b)
x =[a,b]
x.sort()
print(x[0])
big = lambda a,b:a if a > b else b
print(big)