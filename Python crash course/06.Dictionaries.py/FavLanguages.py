favourite_language={
    'Kumar':'Python',
    'Thangapushpam':'C',
    'Royce':'Java',
    "Raissa":"PHP",
}
favourite_language['Raissa']='CPP'
print(favourite_language['Royce'])
print(favourite_language['Raissa'])
print(favourite_language)
#print(favourite_language['Amma'])
print_value=favourite_language.get('Amma')
print(print_value)

for key,value in favourite_language.items():
    print(f'\nKey:{key}')
    print(f'Value:{value}')

for Name, language in favourite_language.items():
    print(f'\n{Name} favourite lanuage:{language}')

for name in favourite_language.keys():
    print(name.upper())

friends=['Kumar','Royce']
for name in favourite_language.keys():
    if name in friends:
        language=favourite_language[name].title()
        print(f'\t{name.title()}, I see you love {language}!')


data = {
    "person": {
        "name": "John",
        "contacts": {
            "email": "john@example.com",
            "phone": "1234567890"
        }
    }
}
print(data['person']['contacts']['phone'])

    