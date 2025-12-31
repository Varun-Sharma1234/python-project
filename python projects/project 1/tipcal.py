# another project in the python so in this project we are going to make the tip calculator. In which we will calculate
#the tip according to the number of people and how much bill has been made 

print("welcome to the tip calculator")
bill = float(input("what is the total of the bill:  "))
tip =  int(input("what percent of tip you want to give 10 12 15 : "))
people = int(input("how many number of people are there for contri: "))
tip_as_percent = tip/100
total_bill = bill*tip_as_percent
bill_per_person = total_bill/people
final_amount = round(bill_per_person)
print(f"so the contri of each person is :{final_amount}")