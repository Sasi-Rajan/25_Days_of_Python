from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import os

question_bank=[]
for question in question_data:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")