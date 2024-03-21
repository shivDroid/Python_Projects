import random

upper_bound = input("Upto  which number would you like to guess?  ")


#Checking if the input is valid
if upper_bound.isdigit():
    upper_bound = int(upper_bound)

    if upper_bound <= 0:
        print("Please enter a number greater than zero")
        quit()
else:
    print("Please provide a integer as input")

random_number = random.randint(0 ,upper_bound)

#randrange - does not include the upper bound 
#randint - does inc


random_number = random.randint(0 ,upper_bound)
guess_counter = 0
user_guess = 0

while True:
    user_guess = input("Guess a number:  ")
    guess_counter += 1 
    #Checking if the input is valid
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please provide a integer as input")
        continue 

    if user_guess == random_number:
        print("you got it right")
        break
    else:
        if user_guess > random_number:
            print("Your guess is greater than the number")
        else:
            print("You were below the number")

print(f"You guesses it in {guess_counter} attempts.")             







