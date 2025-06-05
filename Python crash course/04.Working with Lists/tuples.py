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
