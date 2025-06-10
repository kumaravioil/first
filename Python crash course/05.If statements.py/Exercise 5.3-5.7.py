alien_color=['green','yellow','red']
if "green" in alien_color:
    print("You got 5 points")
else:
    print("You have got 10 points")


if "green" in alien_color:
    print("You got 5 points")
if "yellow" in alien_color:
    print("You got 10 points")
if "red" in alien_color:
    print("You have got 15 points")


age=60# need to know the boundary conditions
if age<=2:
    msg="Baby"
elif age>2 and age<=4:
    msg="Toddler"
elif age>4 and age<=13:
    msg="Kid"
elif age>13 and age<=20:
    msg="Teenager"
elif age>20 and age<65:
    msg="Adult"
elif age>=65:
    msg="Elder"
print(f"Your are {msg}.")

