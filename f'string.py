name="Kumar"
age=42
print("My name is "+ name +" and my age is "+ str(age))
message=f'My name is {name} and my age is {age}'
print(message)
message_format="My name is {} and my age is {}".format(name,age)
print(message_format)
name='thanga pushpam'
print(name.title())
print(name.upper())
print(name.lower())
first_name="Thanga Pushpam"
last_name="Kumar"
full_name=f"{first_name} {last_name}"
print(full_name)
print(f'{full_name.title()}')
print("\tPython")
print("Languages:\n \tPython\n \tC\n \tJavascript")
favourite_language="  Python  "
print(favourite_language.rstrip())
favourite_language=favourite_language.rstrip()
favourite_language=favourite_language.lstrip()
print(favourite_language)
nostarch_url="https://nostarch.com"
nostarch_url=nostarch_url.removeprefix('https://')
nostarch_url=nostarch_url.removesuffix('.com')
print(nostarch_url)