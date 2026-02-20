# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as
#Josiah Hendley
#2/19/26
#Math Quiz

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
import random

# Function that creates and displays the math problem
# It returns both the user's answer and the correct answer
def math_problem():
    # Generate two random numbers
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)

    # Display the problem
    print(num1)
    print("+", num2)
    print("------")

    # Get the user's answer
    user_answer = int(input("Enter your answer: "))

    # Calculate the correct answer
    correct_answer = num1 + num2

    # Return both values
    return user_answer, correct_answer


# Main program
if __name__ == "__main__":
    print("Math Quiz Time!")

    # Call the function
    user_answer, correct_answer = math_problem()

    # Check the answer
    if user_answer == correct_answer:
        print("Correct! Great job!")
    else:
        print("Incorrect.")
        print(f"The correct answer is {correct_answer}.")
