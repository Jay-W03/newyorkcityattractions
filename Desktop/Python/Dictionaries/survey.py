start = '''
Thank you for partcipating in this survey. Let's start with some basic questions.
'''
print(start)

answers = {}

questions = [
"What is your name?",
"How old are you?",
"Where are you from?",
"What's a hobby you have?"
]

for q in questions:
    ans = input(q)
    answers[q]= ans
print(answers)
