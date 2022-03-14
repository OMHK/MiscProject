import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for QuizNum in range(35):
    quizFile = open(f'.\QuizzGenerator\CaptalsQuiz{QuizNum + 1}.txt', 'w')
    answerKeyFile = open(f'.\QuizzGenerator\CapitalsQuiz_answers{QuizNum + 1}.txt', 'w')
    quizFile.write('name:\n\ndate:\n\nPeriod:\n\n')
    quizFile.write(('' * 20) + f'state capitals quiz (Form{QuizNum + 1})')
    quizFile.write('\n\n')
    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
        correctAns = capitals[states[questionNum]]
        wrongAns = list(capitals.values())
        del wrongAns[wrongAns.index(correctAns)]
        wrongAns = random.sample(wrongAns, 3)
        answerOptions = wrongAns + [correctAns]
        random.shuffle(answerOptions)
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f" {'ABCD'[i]}. {answerOptions[i]}\n")
        quizFile.write('\n')
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAns)]}")
quizFile.close()
answerKeyFile.close()
