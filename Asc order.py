x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
z=int(input("Enter the third number: "))
min=mid=max=None
if x<y and x<z:
    min=x
    if y<z:
        mid=y
        max=z
    else:
        mid=z
        max=y
elif y<x and y<z:
    min=y
    if x<z:
        mid=x
        max=z
    else:
        mid=z
        max=x
elif z<x and z<y:
    min=z
    if x<y:
        mid=x
        max=y
    else:
        mid=y
        max=x
print("The numbers in ascending order are: ",min,mid,max)
