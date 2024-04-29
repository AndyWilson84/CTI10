#Andy Wilson
#02/28/2024
#P2HW1
#Basic output with variables

#Pseudocode:
#Get budget (int)
#Get destination (str)
#Get gas (int)
#Get hotel (int)
#Get foot (int)
#Add expenses
#Budget - expenses
#Display results- use example

print("This program calculates and displays travel expenses")
print ()
budget = int(input("What is your budget?: "))
print ()
dest = input("Where is your travel destination?: ")
print ()
gas = int(input("How much will you spend on gas?: "))
print ()
room = int(input("How much will you spend on accommodation?: "))
print ()
food = int(input("How much will you spend on food?: "))
print ()
expenses =(gas + room + food)
print("---------------Travel Eexpenses---------------")

print("Location:\t\t       ",dest)
print(f"Initial Budget:\t\t\t${budget:.2f}")
print(f"Fuel: \t\t\t\t${gas:.2f}")
print(f"Accomodation: \t\t\t${room:.2f}")
print (f"Food:\t\t\t\t${food:.2f}")
print ()
print("----------------------------------------------")
print ()
print(f"Remaining Balance ${budget-expenses:.2f}")
