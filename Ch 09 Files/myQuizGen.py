#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

# trying a different approach to atbs


import random
import itertools
import string
import pyinputplus as pyip

def createHeader(title):
    header = ""
    header = f'US State Capitals Quiz\n\nForm: {title}'
    header += '\n\nName:\n\nDate:\n\nPeriod:\n\n'   
    return header

def createQuestions(theDict,numQ,numA):
    questions = [] #list of [state,{letter:answers}, correct answer]
    # [state,{a:s1, b:s2, c:s3, d:s4},c]
    for _ in range(numQ):
        #get random q
        #this could result in duplicate states
        state,cap = random.choice(list(theDict.items()))
        answers = [cap]
        while len(answers) < numA:
            possA = random.choice(list(theDict.values()))
            if possA not in answers: # don't double up
                answers.append(possA) 

        random.shuffle(answers)
        answerDict={}
        for (c,i) in zip(string.ascii_lowercase[:len(answers)],range(numA)):
            if answers[i] == cap: ans = c
            answerDict.update({c:answers[i]})

        questions.append([state,answerDict,ans])

    return questions
    


def formatQuestions(questions):
    qnum=1
    op=""
    for q in questions:
        op= op+f"\n\nQ{qnum}: What is the capital of {q[0]}?"
        for item, ans in q[1].items():
            op=op+f"\n{item}: {ans}"
        qnum+=1
    op= op + "\n"
    return(op)

def formatAnswers(questions):
    qnum=1
    op=""
    for q in questions:
        op=op+f"\nQ{qnum}: {q[0]} - ans: {q[2]} - {capitals[q[0]]}\n"
        qnum+=1
    return(op)

def writeForms(formname,formnum,questions):
    for f in range(formnum):
        thisform = f'{formname}{f + 1}'
        quizFile = open(f'{thisform}.txt', 'w')
        answerKeyFile = open(f'{formname}{f + 1}-Answers.txt', 'w')

        theHeader = createHeader(thisform)
        theQuestions = formatQuestions(questions)
        quizFile.write(f"{theHeader}{theQuestions}")

        theAnswers = formatAnswers(questions)
        answerKeyFile.write(theAnswers)

        quizFile.close()
        answerKeyFile.close()

    return(None)

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
   'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
   'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 
   'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 
   'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
   'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
   'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'New Mexico': 'Santa Fe', 'New York': 'Albany','North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville',
   'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier',
   'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}



qnum = pyip.inputInt(prompt="How many questions? ",default='2',limit=2,min=1)
#limit to 26 answers a..z
anum = pyip.inputInt(prompt="How many answers? ",default='2',limit=2,min=1,max=26)
formnum = pyip.inputInt(prompt="How many forms? ",default='2',limit=2,min=1)
formname = pyip.inputStr(prompt="Base name? ",blank=False,default="Form",limit=2)

questions = createQuestions(capitals,qnum,anum)


writeForms(formname,formnum,questions)
