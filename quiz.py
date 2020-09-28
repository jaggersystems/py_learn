from question import Question

question_promts = [
    "What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange",
    "What colour are strawberries?\n(a) Red\n(b) Blue\n(c) Orange",
    "what colour are bannans?\n(a)Orange\n(b) Green\n(c) Yellow"
]

questions = [
    Question(question_promts[0], "a"),
    Question(question_promts[1], "a"),
    Question(question_promts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)