# Question 1: Python Modules and Data Handling Assignment

# Task 1: Your Mood Today

import mood_responses
    
while True:
    try:
        mood = input("\nHow are you feeling today? Answer with: Happy, Sad, Excited, or Exit ").title()
        print(mood_responses.mood_response(mood))
        if mood == "Exit":
            break
    except Exception as e:
        print(f"There was an unexpected error: {e}. Please try again.")