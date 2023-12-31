from question import question


questionPrompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    question(questionPrompts[0], "a"),
    question(questionPrompts[1], "c"),
    question(questionPrompts[2], "b")
]

def runTest(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    
runTest(questions)