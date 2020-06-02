import random, os

quiz_quantity = 35

# Dictionary with US states as keys and their capitals as values.
capitals = {"Alabama": "Montgomery",
            "Alaska": "Juneau",
            "Arizona": "Phoenix",
            "Arkansas": "Little Rock",
            "California": "Sacramento",
            "Colorado": "Denver",
            "Connecticut": "Hartford",
            "Delaware": "Dover",
            "Florida": "Tallahassee",
            "Georgia": "Atlanta",
            "Hawaii": "Honolulu",
            "Idaho": "Boise",
            "Illinois": "Springfield",
            "Indiana": "Indianapolis",
            "Iowa": "Des Moines",
            "Kansas": "Topeka",
            "Kentucky": "Frankfort",
            "Louisiana": "Baton Rouge",
            "Maine": "Augusta",
            "Maryland": "Annapolis",
            "Massachusetts": "Boston",
            "Michigan": "Lansing",
            "Minnesota": "Saint Paul",
            "Mississippi": "Jackson",
            "Missouri": "Jefferson City",
            "Montana": "Helena",
            "Nebraska": "Lincoln",
            "Nevada": "Carson City",
            "New Hampshire": "Concord",
            "New Jersey": "Trenton",
            "New Mexico": "Santa Fe",
            "New York": "Albany",
            "North Carolina": "Raleigh",
            "North Dakota": "Bismarck",
            "Ohio": "Columbus",
            "Oklahoma": "Oklahoma City",
            "Oregon": "Salem",
            "Pennsylvania": "Harrisburg",
            "Rhode Island": "Providence",
            "South Carolina": "Columbia",
            "South Dakota": "Pierre",
            "Tennessee": "Nashville",
            "Texas": "Austin",
            "Utah": "Salt Lake City",
            "Vermont": "Montpelier",
            "Virginia": "Richmond",
            "Washington": "Olympia",
            "West Virginia": "Charleston",
            "Wisconsin": "Madison",
            "Wyoming": "Cheyenne"
}

#Creation of quizzes files, answers files and their respective folders to store everything.
def gen_files():
    cwd = os.getcwd()
    if not os.path.exists("C:\\Users\\Iranb\\Desktop\\Python\\quiz generator\\quizzes"): #Creation of quizzes files.
        os.makedirs("C:\\Users\\Iranb\\Desktop\\Python\\quiz generator\\quizzes") #Creation of quiz folder.
        os.chdir("C:\\Users\\Iranb\\Desktop\\Python\\quiz generator\\quizzes") #Change to created quiz folder
        for quiz_num in range(quiz_quantity):
            quiz_object = open("quiz %s.txt" % (quiz_num + 1), "w") #Creation of quiz file.
            quiz_object.write("#%s\nName:\n\nDate:\n\nPeriod:\n\n" % (quiz_num + 1)) #Enumerates the quiz file and creats a header.
            quiz_object.write(" " * 20 + "State Capitals Quiz\n\n") #Quiz title
            quiz_object.close()
    if not os.path.exists("C:\\Users\\Iranb\\Desktop\\Python\\quiz generator\\quizzes answers"): #Creation of answers files.
        os.makedirs("C:\\Users\\Iranb\\Desktop\\Python\\quiz generator\\quizzes answers") #Creation of answer folder.
        os.chdir("C:\\Users\\Iranb\\Desktop\\Python\\quiz generator\\quizzes answers") #Change to created answer folder
        for quiz_num in range(quiz_quantity):
            answer_object = open("answer quiz %s.txt" % (quiz_num + 1), "w") #Creation of answers file.
            answer_object.write("#%s\n\n" % (quiz_num + 1)) #Enumerates the answer file.
            answer_object.write(" " * 20 + "Answers For The Quiz\n\n") #Answer title
            answer_object.close()
    os.chdir(cwd)

def gen_answers():
    states = list(capitals.keys())
    alternatives = {}
    for answer_num in range(len(capitals)):
        correct_answer = capitals[states[answer_num]]
        wrong_answers = list(capitals.values())
        wrong_answers.remove(correct_answer)
        wrong_answers = random.sample(wrong_answers, 3)
        wrong_answers.append(correct_answer)
        random.shuffle(wrong_answers)
        alternatives[states[answer_num]] = wrong_answers
    return alternatives

'''def gen_questions():
    for question_num in range(len(capitals)):
        question_quiz = open("quiz %s.txt" % (question_num + 1), "w")
        question_quiz.append("%s) What is the capital of %s" % (question_num + 1, states[question_num]))
        #Here comes the alternatives
        question_quiz.append()  #The argument here should be the alternatives'''

gen_files()
gen_answers()