import re
filepath = "e:/Devops/Python/Practice/python_practice/2025/sample.txt"
pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
with open(filepath, 'r') as file:
    text = file.read()
ips = re.findall(pattern, text)
ip_list = []
for ip in ips:
    ip_list.append(ip)
print(ip_list)