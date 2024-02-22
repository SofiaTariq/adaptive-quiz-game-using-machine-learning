import random

# Define a list of questions with different difficulty levels
questions = [
    {"question": "What is the capital of France?", "answer": "Paris", "difficulty": 1},
    {"question": "What is 2 + 2?", "answer": "4", "difficulty": 1},
    {"question": "Who wrote 'Romeo and Juliet'?", "answer": "Shakespeare", "difficulty": 2},
    {"question": "What is the powerhouse of the cell?", "answer": "Mitochondria", "difficulty": 2},
    {"question": "What is the square root of 144?", "answer": "12", "difficulty": 3},
    {"question": "What is the chemical symbol for water?", "answer": "H2O", "difficulty": 3}
]

def select_question(questions, current_difficulty):
    #Selects a random question from the list of questions based on current difficulty level.
    
    valid_questions = [q for q in questions if q['difficulty'] == current_difficulty]
    return random.choice(valid_questions)

def play_quiz():
 
    # Main function to play the adaptive quiz game.

    score = 0
    current_difficulty = 1
    
    while True:
        # Select a question based on current difficulty
        question = select_question(questions, current_difficulty)
        
        # Display the question
        print("\nQuestion:", question["question"])
        
        # Get user's answer
        user_answer = input("Your answer: ")
        
        # Check if the answer is correct
        if user_answer.lower() == question["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        
        # Check if it's time to increase difficulty
        if score % 3 == 0:
            current_difficulty += 1
            print("\nCongratulations! Difficulty increased to", current_difficulty)
        
        # Ask if the user wants to continue
        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break
    
    print("\nYour final score is:", score)

# Start the quiz game
play_quiz()
