text = "this is used for win10 build. And all the win10 build are running on hccloud vm's. As hccloud is not having access to internet, all win10 builds are failing."

print(text.replace("win10", "win11"))
list = []
words = text.split(' ')
list.extend(words)
print(list)
print(len(list))
print(text.capitalize())

with open("E:/python/python_for_devops/2025/updated.txt", 'w') as data:
    data.write(text.replace("win10", "win11"))
    data.close()