def starprinting(i):
    for k in range(i):
        for j in range(0, k + 1):
            print('*', end = "")
        print()
    for k in range(1,i):
        for j in range(k, i):
            print('*', end = "")
        print()
        
print(starprinting(5))
