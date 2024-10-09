import random

number = random.randint(1,10)
attempts = 3
count = 1


while count <= attempts:
    guess = int(input("Guess a number between 1-10: "))
    if guess > number: 
        print ("too high")
    elif guess < number:
        print ("too low")
    else:
        print ("correct")  
        break
    count += 1
print("womp womp")   