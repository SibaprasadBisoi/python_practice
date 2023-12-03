country_code = {"india": 91,
                "usa": 1,
                "uk": 44}
print(list(sorted(country_code.values())))
print(country_code.get('india', 'not_found'))
print(country_code.get('japan', 'not_found'))
country_code.setdefault('japan', '81')
print(country_code)
print(country_code["india"])
# print(country_code["india", "japan", "usa"])
print(list(country_code.values()))