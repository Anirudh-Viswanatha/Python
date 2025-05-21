from question_model import Question
from data import question_data1 #from data import question_data
from quiz_brain import QuizBrain

question_bank = []

no_of_questions = (len(question_data1))  #no_of_questions = (len(question_data)) use this for question bank 1   # We could optimize by skipping this step and instead write "for i in question_data" ,here question_data is from data file. in sucn case i with become the dictionary in question_data

for i in range(no_of_questions):
    single_question = question_data1[i]["question"]   #single_question = question_data[i]["text"] use this for question bank 1
    single_answer = question_data1[i]["correct_answer"]   # single_answer = question_data[i]["answer"] use this for question bank 1
    new_question = Question(single_question, single_answer) # creating object "new_question" from class "Question"
    question_bank.append(new_question)

# print(question_bank[0].text)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print ("You've completed the quiz!")
print (f"your final score is: {quiz.score}/{quiz.question_number}")
