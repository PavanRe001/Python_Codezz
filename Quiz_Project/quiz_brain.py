class QuizBrain:
    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.questions_list = questions
    def still_has_questions(self):
        return self.question_no < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_no]
        self.question_no += 1
        user_answer=input(f"Q.{self.question_no}: {current_question.text} (True or False)")
        self.check_answer(user_answer,current_question.answer)
    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score+=1
        else:
            print("Sorry, that was wrong.")
        print(f'the correct answer was:{correct_answer}')
        print(f'Yor current score is {self.score}/{self.question_no}')
        print('\n')


