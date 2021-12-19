import random 
rand = random.randrange(1,9)
chances = 5
game = 0
for i in range(5) :
    reply = input("Enter a number :- ")
    reply = int(reply)
    if reply == rand:
        print("You guessed correct")
        game = 1
        break
    
    if reply != rand:
        if reply < rand:
            print("Incorrect your answer is too low")
            game =0
            continue
        if reply > rand:
            print("Incorrect your answer is too high")
            game =0
            continue
        
