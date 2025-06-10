dimension=(50,40)
print(dimension[0])
print(dimension[1])
#dimension[0]=25# tuple doenot allow item to be changed
dimension=[200,50]
print(dimension)

dimension=[45,20,78]
print("The original dimensions are:")
for item in dimension:
    print(item)
dimension=[60,54,67]
print("The new dimensions are:")
for item in dimension:
    print(item)

name = "Eric"
new_name = name.lower()
name = "John"
print(new_name)


numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:  # If the number is even
        numbers.remove(num)
print(numbers)


my_string = "Python"
sliced_string = my_string[-1:0:-1]
print(sliced_string)
