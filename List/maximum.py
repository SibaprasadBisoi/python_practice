def maxi(a, b):

    if a >= b:
        return a
    else:
        return b
a, b = 87, 99
print(maxi(a, b))
print(max(a, b))
print(a if a>=b else b)
x =[a,b]
x.sort()
print(x[-1])
big = lambda a,b:a if a > b else b
print(big)

