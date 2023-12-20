def diamond(rows):
    n = 1
    for i in range(1, rows+1):
        for j in range(1, (rows -i)+1):
            print(end = ' ')
diamond(10)