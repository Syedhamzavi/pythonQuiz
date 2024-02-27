import time
import random
from colorama import init, Back

init(autoreset=True)

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question_number):
        question = self.questions[question_number]['question']
        options = self.questions[question_number]['options']

        print(Back.CYAN + f"\nQuestion {question_number + 1}: {question}" + Back.RESET)

        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

    def get_user_answer(self):
        while True:
            try:
                answer = input("Enter your answer: ").strip()
                if answer.lower() in ['1', '2', '3', '4']:
                    return int(answer)
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")

    def check_answer(self, question_number, user_answer):
        correct_answer = self.questions[question_number]['correct']
        if user_answer == correct_answer:
            print(Back.GREEN + "Correct!" + Back.RESET + "\n")
            self.score += 1
        else:
            correct_option = self.questions[question_number]['options'][correct_answer - 1]
            print(Back.RED + f"Wrong! The correct answer is {correct_answer}: {correct_option}" + Back.RESET + "\n")

    def run_quiz(self):
        random.shuffle(self.questions)
        start_time = time.time()

        for i in range(len(self.questions)):
            self.display_question(i)
            user_answer = self.get_user_answer()
            self.check_answer(i, user_answer)

        end_time = time.time()
        total_time = end_time - start_time

        print(Back.MAGENTA + f"\nYour final score is: {self.score}/{len(self.questions)}" + Back.RESET)
        print(f"Total time taken: {total_time:.2f} seconds")

if __name__ == "__main__":
    quiz_questions = [
        {
            'question': 'What is a linked list?',
            'options': ['A linear data structure', 'A non-linear data structure', 'A tree structure', 'A graph structure'],
            'correct': 1
        },
        {
            'question': 'Which data structure follows the Last In First Out (LIFO) principle?',
            'options': ['Queue', 'Stack', 'Array', 'Linked List'],
            'correct': 2
        },
        {
            'question': 'What is the difference between a stack and a queue?',
            'options': ['Stack follows LIFO, Queue follows FIFO', 'Stack follows FIFO, Queue follows LIFO', 'Both follow LIFO', 'Both follow FIFO'],
            'correct': 1
        },
        {
            'question': 'Which data structure is suitable for implementing a recursive algorithm?',
            'options': ['Array', 'Linked List', 'Stack', 'Queue'],
            'correct': 3
        },
        {
            'question': 'What is the time complexity of searching for an element in a binary search tree?',
            'options': ['O(1)', 'O(log n)', 'O(n)', 'O(n log n)'],
            'correct': 2
        },
        {
            'question': 'In the context of hash tables, what is collision resolution?',
            'options': ['The process of creating a hash function', 'The process of handling hash function collisions', 'The process of resizing the hash table', 
                        'The process of searching for a key'],
            'correct': 2
        }
    ]

    quiz = Quiz(quiz_questions)
    quiz.run_quiz()
