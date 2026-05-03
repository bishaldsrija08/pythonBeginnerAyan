import time
quiz = [
    {
    "question": "What is the capital of France?",
    "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
    "ansser": "c"
    },
    {
    "question": "Which planet is known as the Red Planet?",
    "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
    "ansser": "b"
    },
    {
    "question": "What is the largest mammal?",
    "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus"],
    "ansser": "b"
    }
]

time_limi = 10
score = 0

print("Welcome to the Quiz!")
print("You have", time_limi, "seconds to answer each question.")

for i, q in enumerate(quiz):
    print(f"Question {i + 1}: {q['question']}")
    for option in q['options']:
        print(option)
        
    start_time = time.time()
    user_answer = input("Your answer (A, B, C, D): ").lower()
    end_time = time.time()
    time_taken = end_time - start_time

    if time_taken > time_limi:
        print("Time's up! You took too long to answer.")
    elif user_answer == q['ansser']:
        print("Correct!")
        score += 1

print(f"Quiz completed! Your score is: {score}/{len(quiz)}")