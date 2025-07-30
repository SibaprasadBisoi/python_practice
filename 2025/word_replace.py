file = "E:/Devops/Python/Practice/python_practice/2025/sample.txt"
with open(file, 'r')as f:
    text = f.read()
    new_text = text.replace("This", "that")
    f.close()
print(new_text)
with open(file, "w")as t:
    t.write(new_text)
    t.close()