#Andy Wilson
#03/29/2024
#P4HW1
#Scores using loops


score = int(input("How many Scores do you want to enter: "))
print()
scores = []

for num in range(score):
    scor = int(input("Enter score: "))
    if scor > 100:
       print()
       y = int(input("INVALID Score entered!!!\nScore should be between 0 and 100\n Enter score again: "))
       scores.append(y)
    elif scor < 1:
       print()
       x = int(input("INVALID Score entered!!!\nScore should be between 0 and 100\n Enter score again: "))
       scores.append(x)
    else:
        scores.append(scor)




print()
print("---------------Results--------------------")
low_score = min(scores)
print (f"Lowest  score:              {low_score:.1f}")

scores.remove(low_score)

print (f" Modified List: {scores}")

score_len = len(scores)
score_sum = sum(scores)

average = score_sum / score_len
print (f"Score Average:              {average:.2f}")

if average >= 90:
    print('Your score is: A')
elif average >= 80:
    print('Your score is: B')
elif average >=70:
    print('Your score is: C')
elif average >=66:
    print('your score is: D')
else:
    print('Your score is: F')

print("------------------------------------------")
