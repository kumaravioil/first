cars=['Indica',"BMW",'Honda',"Suzuki"]
print(cars)
cars[0]="Lambo"#Modifying element using index and value
print(cars)
cars.append('RR')
print(cars)
family=[]#append to add individual items one by one in the empty list
family.append('Kumar')
family.append("ThangaPushpam")
family.append("Raissa")
family.append('Royce')
print(family)
family.insert(0,'Ramasamy')#insert the item using index and value
family.insert(1,'Pappa')
print(family)
del cars[0]#DEl used to remove the item if you know the index of an item
print(cars)
del cars[-1]
print(cars)# we can not use the value deleted using DEL command
popped_car=cars.pop()#Use POP to remove the last item in the list temporarily
print(cars)
print(popped_car)
last_car=f'The last owned car was {popped_car.upper()}'
print(last_car)
print(cars)
popped_car2=cars.pop(1)#POP uses index to remove item from the index number
print(cars)
print(popped_car2)
cars=['Indica',"BMW",'Honda',"Suzuki"]
print(cars)
cars.remove("Indica")#Remove is used to delete item by value
print(cars)
bmw="BMW"
cars.remove(bmw)
print(cars)
print(f'{bmw} is very expensive car.So I removed it')