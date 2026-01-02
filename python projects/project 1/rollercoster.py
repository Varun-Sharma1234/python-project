print("wlecome to the ride: ")
height =int(input("pls enter your height in the cm: "))
bill = 0 
if height>=120:
    print("u can ride the ride")
    age = int(input("pls enter your age: "))
    if age <12:
        bill = 20
        print("u have to pay 20")
    elif age >=18:
        bill = 30 
        print("u have to pay 30")

    wants_photo = input("do u want a photo taken y or n:")
    if wants_photo == "y":
        bill += 3
    print(f"your final bill is {bill}")

else:
    print("chal bae bone ")