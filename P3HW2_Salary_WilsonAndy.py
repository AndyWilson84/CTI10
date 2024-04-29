#Andy Wilson
#03/18/2024
#P3HW2_Salary_
#Salary



name = input("Enter employee's name: ")
hw = float(input("Enter number of hours worked: "))
pr = float(input("enter employee's pay rate: "))

var1 = hw
var2 = pr
var3 = hw - 40
if hw > 40:
     (hw-40)
else:
      var3 = 0
var4 = pr* 1.50 * var3
if var3 > 1:
     (pr* 1.50 * var3)
else:
     var4 = 0
var5 = hw * pr
var6 = var4 + var5

print ("--------------------------------------------------------------------------------")
print ("Employee name:",  name)
print()
print ("Hours Worked   Pay Rate      OverTime     OverTime Pay     RegHour Pay     Gross Pay")
print ("--------------------------------------------------------------------------------")
print (f'{var1:.1f}             {var2:.1f}         {var3:.1f}          {var4:.2f}            ${var5:.2f}        ${var6:.2f}')
