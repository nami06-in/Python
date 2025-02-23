"""
    A program that has 12 True/False Questions.
    The Question Category is Computer Science.
    If you want to change the category:-
       Use Open Trivia DB to Get New Questions:- (https://opentdb.com/)
       click API at the top right corner -> select number of questions, category and difficulty -> CLICK generate api -> 
       go to the link browser -> copy the questions generated -> paste it on question_data then click code -> 
       reformat code, change the main.py accordingly

"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
