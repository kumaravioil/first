# 4.3 print numbers to 20
# for num in range(1,21):
#     print(num)

#4.4 & 4.5 list number up to million
# num=list(range(1,1000001))
# for x in num:
#     print(x) 
# print(min(num))
# print(max(num))
# print(sum(num))

#4.6 printing odd numbers
# odd_num=list(range(1,20,2))
# for x in odd_num:
#     print(x)

# #4.7 multiples of 3
# multiples=list(range(3,30,3))
# for x in multiples:
#     print(x)

#4.8 cube from 1 to 10
cubes=list(range(1,11))
for x in cubes:
    cubes=x**3
    print(cubes)

# 4.8 second method
cube=[]
for i in range(1,11):
    cube.append(i**3)
print(cube)    


#4.9 cube comprehension
cube=[value**3 for value in range(1,11)]
print(cube)
for n in cube:
    print(n)