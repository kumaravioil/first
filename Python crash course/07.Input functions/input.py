""" name=input("Enter your name: ")
if name=="Kumar":
    print(f"Hello!, {name}")
else:
    print("Hello!,Dude") """

""" current_num=int(input("Enter the number below 10: "))
while current_num<=10:
    print(current_num)
    current_num+=1 """

""" prompt="Tell me something I will repeat it for you:"
prompt+="Write quit if you want to quit:\n "
msg1="Kumar"
while msg1!='Quit':
    msg1=input(prompt)
    print(msg1) """

""" current_number=0
while current_number<=10:
    current_number+=1
    if current_number%2==0:
        continue
    print(current_number) """

user_name=input("Enter your user name: ")
if len(user_name)>12:
    print("User Name can't be more than 12 character")
elif not user_name.find(" ")==-1:
    print("User Name can't contain spaces")
elif  not user_name.isalpha():
    print("User Name can't contain numbers")
else:
    print(f'Welcome {user_name.upper()}')