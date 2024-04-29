#Andy Wilson
#03/27/2024
#P4LAB2
#LAB: Output Range with increment of 5 Int and string 


print("incerements by 5s")
print()
#Get two integer values from user
var1 = int(input("Enter lowest starting point: "))
var2 = int(input("Enter largest end point: "))

#While var1 is larger, allow user to re-enter the values
while var1 >= var2:
    print("First number must be smaller try again.")
    var1 = int(input("Enter lowest starting point: "))
    var2 = int(input("Enter largest end point: "))

#While Loop has broken. Values entered correctly


#Third number "5" will add 5 from var1 until var2 if it can.
for num in range(var1,var2+1,5):
    print(num, end=" ")

# print(num,end= " ") will allow to put numbers left to right.
