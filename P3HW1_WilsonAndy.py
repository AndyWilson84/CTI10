#Andy Wilson
#03/15/2024
#P3HW1
#Debug



# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
grades = []

mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# add grades entered to a list

grades.append(mod_1) 
grades.append(mod_2)
grades.append(mod_3)
grades.append(mod_4)
grades.append(mod_5)
grades.append(mod_6)
print()
# TO DO: determine lowest, highest , sum and average for grades
print ("---------------Results--------------------")
low = min(grades)
print (f"Lowest  grade:        {low:.1f}")
high = max(grades)
print (f"Highest grade:        {high:.1f}")
grade_sum = sum(grades)
print (f"Sum of grade:         {grade_sum:.1f}")
grade_len = len(grades)
avg = grade_sum / grade_len
print (f"Average:              {avg:.2f}")
print ("-----------------------------------------")
# determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >=70:
    print('Your grade is: C')
elif avg >=66:
    print('your grade is: D')
else:
    print('Your grade is: F')

# TO DO: finish this



