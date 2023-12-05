import json
dict = {"siba": "devops",
        "gautam": "devloper"}
with open("test.txt", "w") as file:
    file.write(json.dump(dict))