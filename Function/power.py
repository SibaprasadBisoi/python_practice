def power(N, p):
    if p == 0:
        return 1
    else:
        return(N*power(N, p-1))
print(power(10, 5))


