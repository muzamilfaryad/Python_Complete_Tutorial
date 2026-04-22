# Question class to store each question and its correct answer
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


# List of questions (prompts)
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

# Creating Question objects
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


# Function to run the quiz
def run_test(questions):
    score = 0

    for question in questions:
        answer = input(question.prompt)  # take user input

        if answer.lower() == question.answer:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


# Run the quiz
run_test(questions)