import winrm
session = winrm.Session('http://127.0.0.1:5985/wsman', auth=('Prasad', 'Benir'))
result = session.run_cmd('ipconfig', [])
print(result.std_out.decode())