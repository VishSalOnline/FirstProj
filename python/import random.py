import random
randomNumber= random.randint(1,100)
print(randomNumber)
userGuess=None
count=0
while userGuess!=randomNumber:
    count+=1
    userGuess=int(input("Enter the Number : "))
    if userGuess==randomNumber:
        print("You guessed it right.")
    else:
        print("You guessed it wrong.")
        if userGuess>=randomNumber:
            print("You guessed number greater than number.")
        else:
            print("You guessed number lesser than number.")
print(f"You guessed it right in {count} counts.")
with open("HighestScore.txt","r") as file:
    HighestScore=file.read()
if count<int(HighestScore):
    print("You are the Highest Scorer of the game!!!")
    print(f"Previous Highest score was {HighestScore}")
    with open("HighestScore.txt","w") as file:
        file.write(str(count))
with open("HighestScore.txt","r") as file:
    HighestScore=int(file.read())
print(HighestScore)