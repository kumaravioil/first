cars=['maruti','audi','lambo','indica','bmw']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())


        
banned_user=['Kumar',"Royce"]
user='Kumar'
if user not in banned_user:
    print(f'{user.title()} can post in the forum')
else:
    print(f'{user.title()} cannot post in the forum')

