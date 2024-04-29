#Andy Wilson
#04/08/2024
#P4HW2_Salary_
#Salary_Loops



name = 0
hw = 0
pr = 0
emp_num = 0
p_ot = 0
p_rh = 0
p_gross = 0
print()
while name !="Done":
     name = input('Enter employee\'s name or "Done" to terminate: ')
     if name !="Done":
          hw = float(input(f"How many hours did {name} work?: "))
          pr = float(input (f"What is {name}'s pay rate?: "))
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
          var5 = 40 * pr
          if hw > 40:
               (40 * pr)
          else:
              var5 = (hw * pr)
          var6 = var4 + var5
          emp_num += 1
          p_ot += var4
          p_rh += var5
          p_gross += var6
          print()
          print ("Employee name:",  name)
          print()
          print ("Hours Worked   Pay Rate      OverTime     OverTime Pay     RegHour Pay     Gross Pay")
          print ("--------------------------------------------------------------------------------")
          print (f'{var1:.1f}             {var2:.1f}         {var3:.1f}          {var4:.2f}            ${var5:.2f}        ${var6:.2f}')
          print()
     else:
          print()
          print(f"number of employees entered: {emp_num}")
          print(f"Total amoun paid for overtime: ${p_ot:.2f}")
          print(f"Total amount paid for regular hours: ${p_rh:.2f}")
          print(f"Total amount paid in gross: ${p_gross:.2f}")

