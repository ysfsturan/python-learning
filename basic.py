print("enter your name:")
name = input ()
list= [name]
print(f"hello: {name}")
print("enter your age:")
age = input ()
list.append(age)
print(f"your age is: {age}")
print(list)

if 18 <= int(age) <= 25:
    print("you are eligible for the program")

else:
   print("you are not eligible for the program")
