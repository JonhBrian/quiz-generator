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
        os.chdir("C:\\Users\\Iranb\\Desktop\\Python\\quiz generator\\quizzes") #Change to created quiz folder.
        for quiz_num in range(quiz_quantity):
            quiz_object = open("quiz %s.txt" % (quiz_num + 1), "w") #Creation of quiz file.
            quiz_object.write("#%s\nName:\n\nDate:\n\nPeriod:\n\n" % (quiz_num + 1)) #Enumerates the quiz file and creats a header.
            quiz_object.write(" " * 40 + "States Capitals Quiz\n\n") #Quiz title.
            quiz_object.close()
    if not os.path.exists("C:\\Users\\Iranb\\Desktop\\Python\\quiz generator\\quizzes answers"): #Creation of answers files.
        os.makedirs("C:\\Users\\Iranb\\Desktop\\Python\\quiz generator\\quizzes answers") #Creation of answer folder.
        os.chdir("C:\\Users\\Iranb\\Desktop\\Python\\quiz generator\\quizzes answers") #Change to created answer folder.
        for quiz_num in range(quiz_quantity):
            answer_object = open("answer quiz %s.txt" % (quiz_num + 1), "w") #Creation of answers file.
            answer_object.write("#%s\n\n" % (quiz_num + 1)) #Enumerates the answer file.
            answer_object.write(" " * 40 + "Answers For The Quiz\n\n") #Answer title.
            answer_object.close()
    os.chdir(cwd)

#Generates 4 alternatives for each state which 3 are wrong and only 1 is right.
def gen_answers(states_answers): 
    all_alternatives = {}
    for answer_num in range(len(capitals)):
        correct_answer = capitals[states_answers[answer_num]]
        wrong_answers = list(capitals.values())
        wrong_answers.remove(correct_answer)
        wrong_answers = random.sample(wrong_answers, 3)
        wrong_answers.append(correct_answer)
        random.shuffle(wrong_answers)
        all_alternatives[states_answers[answer_num]] = wrong_answers
    return all_alternatives

#Generates all the questions and write them in their respective quiz files.
#Moreover, also writes the answers in their repective answer quiz files.
def gen_questions(states_questions):
    for quiz_num in range(quiz_quantity):
        random.shuffle(states_questions)
        question_quiz = open("C:\\Users\\Iranb\\Desktop\\Python\\quiz generator\\quizzes\\quiz %s.txt"
                                % (quiz_num + 1), "a")
        answer_quiz = open("C:\\Users\\Iranb\\Desktop\\Python\\quiz generator\\quizzes answers\\answer quiz %s.txt"
                            % (quiz_num + 1), "a")
        #Here is where all the questions are created, shuffled and written in the quiz files.
        for question_num in range(len(capitals)):
            question_quiz.write("%s. What is the capital of %s\n\n"
                                % (question_num + 1, states_questions[question_num]))
            alternatives = gen_answers(states_questions)
            question_quiz.write("A) " + alternatives[states_questions[question_num]][0] +
                              "\nB) " + alternatives[states_questions[question_num]][1] +
                              "\nC) " + alternatives[states_questions[question_num]][2] +
                              "\nD) " + alternatives[states_questions[question_num]][3] + "\n\n")
            #Here is where all the answers are written in the answers files.
            if capitals[states_questions[question_num]] == alternatives[states_questions[question_num]][0]:
                answer_quiz.write("%s. %s\n" % ((question_num + 1), "A"))
            elif capitals[states_questions[question_num]] == alternatives[states_questions[question_num]][1]:
                answer_quiz.write("%s. %s\n" % ((question_num + 1), "B"))
            elif capitals[states_questions[question_num]] == alternatives[states_questions[question_num]][2]:
                answer_quiz.write("%s. %s\n" % ((question_num + 1), "C"))
            elif capitals[states_questions[question_num]] == alternatives[states_questions[question_num]][3]:
                answer_quiz.write("%s. %s\n" % ((question_num + 1), "D"))
        question_quiz.close()
        answer_quiz.close()

states = list(capitals.keys())

gen_files()
gen_questions(states)