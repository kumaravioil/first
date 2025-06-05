players=['Kapil','Sachin','Davis','Swati','Anil','Kumar','Royce']
print(players[0:2])
print(players[2:])
print(players[:3])
print(players[-3:])
print(players[:-1:2])
print("Here are the first three players:")
for player in players[:3]:
    print(player.upper())

my_book=['Python','java','cpp','c']
friend_book=my_book[:]
print(my_book)
print(friend_book)
my_book.append('php')
friend_book.append('SQL')
print(my_book)
print(friend_book)

my_book=['Python','java','cpp','c']
friend_book=my_book
print(my_book)
print(friend_book)
my_book.append('php')
friend_book.append('SQL')
print(my_book)
print(friend_book)
