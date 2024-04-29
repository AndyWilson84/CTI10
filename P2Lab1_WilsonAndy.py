#Andy Wilson
#2/28/2024
#P2Lab1
#Math expression and f-string

#Get info from user
mpg = float (input ("enter the car's mpg:"))
cost = float(input("Enter the car's for a gallon of gas: "))
print()
#Calculate cost to drive 20, 75, 500 miles
miles_20 = (20/mpg) * cost
miles_75 = (75/mpg) * cost
miles_500 = (500/mpg) * cost
print()
#Output infor to user
print(f"The cost to drive 20 miles is ${miles_20:.2f}\n")
print (f"The cost to drive 75 miles is ${miles_75:.2f}\n")
print(f"The cost to drive 500 miles is ${miles_500:.2f}\n")

