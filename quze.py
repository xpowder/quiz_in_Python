def ask_question(question, correct_question):
    answer = input(question).lower()
    
    
    while True:
        if answer == correct_question:
            print("Correct")
            return True
        else:
            print("Incorrect. Try again.")
        answer == input(question).lower()
        


questions = [
    ("How do you create a block in Python? Enter the correct answer: ", "indentation"),
    ("When declaring variable in Python, can a variable name contain white space (True/False)? Enter the correct answer: ", "true"),
    ("In Python, how can you convert a number to a string? Enter the correct answer: ", "str"),
    ("n Integer - int in Python can be converted to type Float by using the float function (True/False)? Enter the correct answer: ","true"),
    ("An enumerate function is used to provide the index of the current iteration of a for loop (True/False)? Enter the correct answer: ","true"),
    ("args passed to the functions can accept the key-value pair (True/False)? Enter the correct answer: ", "false"),
]


print("Welcome to the game!")

player = input("Do you want to play this game? (y/n): ").lower()
if player != "y":
    print("Thank you for the answer!")
    quit()


for question, correct_question in questions:
    ask_question(question, correct_question)
print("Congratulations! You've answered all questions correctly.")
