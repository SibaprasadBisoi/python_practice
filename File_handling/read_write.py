with open("E:/DevOps/Python/Practice/test.txt", "r") as f:
    content = f.read()
    content1 = f.read(1)
    print(content)
    print(content1)
with open("E:/DevOps/Python/Practice/python_practice/File_handling/test1.txt", 'w') as w:
    w.write(content)
    w.close()