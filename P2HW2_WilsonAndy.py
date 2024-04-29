#Andy Wilson
#03/04/2024
#P2HW2
#Design a program of List

grades = []

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: ")) 
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))
grades.append(module1) 
grades.append(module2)
grades.append(module3)
grades.append(module4)
grades.append(module5)
grades.append(module6)
print()
print("---------------Results--------------------")
low_grade = min(grades)
print (f"Lowest  grade:        {low_grade:.2f}")
high_grade = max(grades)
print (f"Highest grade:        {high_grade:.2f}")
grade_sum = sum(grades)
print (f"Sum of grade:         {grade_sum:.2f}")
grade_len = len(grades)
average = grade_sum / grade_len
print (f"Average:              {average:.2f}")
print("------------------------------------------")
