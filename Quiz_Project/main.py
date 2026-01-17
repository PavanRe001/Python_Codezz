from data import question_data
from question_model import quiz
from quiz_brain import QuizBrain
question_bank=[]
for values in question_data:
    q_text = values["text"]
    q_answer = values["answer"]
    vessel=quiz(q_text,q_answer)
    question_bank.append(vessel)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f'You have completed the quiz.Your total Score is {quiz.score}/{len(quiz.questions_list)}')
