print("welcome to the python pizza delivery app")
size = input("what size of pizza do you want S M or L: ")
add_pepperoni = input("do you want pepperoni y or n: ")
extra_cheese = input("do you want extra cheese y or n: ")
bill = 0 

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("invalid size")

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1
print(f"your final bill is {bill}")

