print("Quiz game ")
playing = input("Do you want to play? Y/N")

   
if playing.lower() != 'y':
    quit()

print("Okay lets play :) ")
score = 0 

answer = input("what dose CPU stand for ? ").lower()
if answer == "central processing unit":
    print("Correct! ")
    score += 1
else: 
    print("Incorrect !!")

    
answer = input("what dose GPU stand for ? ").lower()
if answer == "graphics processing unit":
    print("Correct! ")
    score += 1
    
else: 
    print("Incorrect !!")
    
    
answer = input("what dose RAM stand for ? ").lower()
if answer == "random access memory":
    print("Correct! ")
    score += 1

else: 
    print("Incorrect !!")
    

print("You got : " + str(score) + " questions correct!")
print("You got : " + str((score / 3) * 100 ) + "%")

    
    