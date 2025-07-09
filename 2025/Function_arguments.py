def average(a=6, b=7):
    print("The averageis ", (a+b)/2)

average()
average(b=90)

def name(fname, mname= "prasad", lname= "bisoi"):
    print("Hello,", fname, mname, lname)

name(fname = "siba")
average(b=10, a=100)

def average1(*numbers):
    sum = 0
    for i in numbers:
        sum = sum +i
    # print("The average is:", sum / len(numbers))
    return sum / len(numbers)
c = average1(1,3,6,7,8,100)
print(c)
print(int(c))

def name(**name):
    print("Hello:", name["fname"], name["mname"], name["lname"])
name(fname="siba",mname= "prasad",lname= "bisoi")
