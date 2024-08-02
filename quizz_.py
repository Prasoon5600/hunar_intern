# Define the questions and answers
quiz_data = [
    {"question": "What is the capital of France?", "options": ["A. Paris", "B. Rome", "C. Berlin", "D. Madrid"], "answer": "A"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"], "answer": "B"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"], "answer": "A"},
    {"question": "What is the smallest prime number?", "options": ["A. 0", "B. 1", "C. 2", "D. 3"], "answer": "C"},
    {"question": "Which element has the chemical symbol 'O'?", "options": ["A. Oxygen", "B. Gold", "C. Hydrogen", "D. Carbon"], "answer": "A"}
]

def run_quiz(quiz_data):
    score = 0
    total_questions = len(quiz_data)

    for idx, item in enumerate(quiz_data, start=1):
        print(f"Question {idx}: {item['question']}")
        for option in item['options']:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").upper()

        if user_answer == item['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {item['answer']}\n")

    print(f"Quiz finished! Your final score is {score}/{total_questions}.")

# Run the quiz
run_quiz(quiz_data)


