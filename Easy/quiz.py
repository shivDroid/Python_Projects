print("Welcome to the quiz!")

play_cnf = input("Will you like to continue playing the game?  ").lower()

if play_cnf != "yes":
    quit()

print("Okay! Let us play")

score_counter = 0 
total_question_counter = 0

answer1 = input("What does CPU stand for? ").lower()
if answer1 == "central processing unit":
    print("Correct")
    score_counter = score_counter + 1 
else:
    print("Incorrect")
total_question_counter = total_question_counter + 1        

answer1 = input("What does RAM stand for? ").lower()
if answer1 == "random access memory":
    print("Correct")
    score_counter = score_counter + 1 
else:
    print("Incorrect")
total_question_counter = total_question_counter + 1  

answer1 = input("What does OS stand for? ").lower()
if answer1 == "operating system":
    print("Correct")
    score_counter = score_counter + 1 
else:
    print("Incorrect")
total_question_counter = total_question_counter + 1  

answer1 = input("What does AI stand for? ")
if answer1 == "artificial intelligence":
    print("Correct")
    score_counter = score_counter + 1 
else:
    print("Incorrect")
total_question_counter = total_question_counter + 1  

print(f"Your final score is {score_counter} and your percentage is {(score_counter/total_question_counter)*100}")    