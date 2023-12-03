dict = {'ravi': '10', 'rajnish': '9',
        'sanjeev': '15', 'yash': '2', 'suraj': '32'}
mykeys = list(dict.keys())
print(mykeys)
mykeys.sort()
sorted_dict= {i:dict[i] for i in mykeys}
print(sorted_dict)