""" def formated_name(first_name,last_name):
    full_name=f'{first_name} {last_name}'
    return full_name.upper()


director=formated_name("Kumar","Ramasamy")
print(director)
print(formated_name("Kumar","Ramasamy"))
 """

""" def fullname(first_name,last_name,middle_name=""):
    if middle_name:
        full_name=f'{first_name} {middle_name} {last_name}'
    else:
        full_name=f'{first_name} {last_name}'
    return full_name

name=fullname("Kumar","Ramasamy","sant")
print(name) """

def city_country(city,country):
    name=f'{city.upper()},{country.upper()}'
    return name

print(city_country("Delhi","India"))
print(city_country("Paris","France"))
print(city_country("Moscow","Russia"))

