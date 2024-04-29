#Andy Wilson
#4/22/2024
#P5HW
#User-defined functions

import random

   #Call all other functions from here
    
def addrandom():

    #Create random nums
    rand_num1 = random.randint(1,100)
    rand_num2 = random.randint(1,100)
    add = rand_num1 + rand_num2
    print(f"{rand_num1}\n+ {rand_num2}")
    answer= int(input(f"Enter answer: "))
    num_count = 1
    while add != answer:
        num_count += num_count    
        if add < answer:
            print(f"{answer} is too high")
        if add > answer:
            print(f"{answer} is too low")
        answer= int(input(f"Enter answer: "))
    print("Congratulations!!! Your answer is correct.")
    print(f"Number of guesses: {num_count}")

def subrandom():
    rand_num1 = random.randint(1,100)
    rand_num2 = random.randint(1,100)
    sub = rand_num1 - rand_num2
    print(f"{rand_num1}\n- {rand_num2}")
    answer= int(input(f"Enter answer: "))
    num_count = 1
    while sub != answer:
        num_count += num_count
        if sub < answer:
            print(f"{answer} is too high")
        if sub > answer:
            print(f"{answer} is too low")
        answer= int(input(f"Enter answer: "))
    print("Congratulations!!! Your answer is correct.")
    print(f"Number of guesses: {num_count}")
    
def main():
    print("Welcome to Math Quiz")
    print()
    print()

    print("MAIN MENU")
    print("------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")




      
    option = " " 

    #Runs first time automatically
            
    while option != "3":
        if option == "1":
           addrandom()


        if option == "2":
            subrandom()
        

        
            
        print("Choose 1, 2, 3")
        print("Enter '3' to quit")
        print()
        option =input(f"Please choose one of the menu options: ")
    #Loop breaks
    print("Thank you for playing...\nBye!!")


 
    
#call the main
main()



