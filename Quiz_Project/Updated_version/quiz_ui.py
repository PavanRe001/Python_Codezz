from tkinter.font import ITALIC
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
from tkinter import *

class QuizInterface:
    def __init__(self,quiz:QuizBrain):#<----quiz:'QuizBrain' ensures you dont do any error by passing smtg else
        self.quiz_brain = quiz
        self.window=Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.canvas=Canvas(width=300,height=250)
        self.right=PhotoImage(file="images/true.png")
        self.wrong=PhotoImage(file="images/false.png")
        self.questions=self.canvas.create_text(150,125,text="Empty",font=("Arial",20,ITALIC),width=280)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)
        self.true=Button(image=self.right,command=self.correct_answer)
        self.false=Button(image=self.wrong,command=self.wrong_answer)
        self.true.grid(row=2, column=0)
        self.false.grid(row=2, column=1)
        self.score=Label(text=f"Score: 0",fg="white",bg=THEME_COLOR,font=("Arial",15))
        self.score.grid(row=0,column=1)
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background='white')
        if self.quiz_brain.still_has_questions():
            self.score.config(text=f"Score: {self.quiz_brain.score}", fg="white", bg=THEME_COLOR, font=("Arial", 15))
            q_text=self.quiz_brain.next_question()
            self.canvas.itemconfig(self.questions,text=q_text)
        else:
            self.canvas.itemconfig(self.questions,text="You've reached the end of the Quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")


    def correct_answer(self):
        user_answer='true'
        self.give_feedback(self.quiz_brain.check_answer(user_answer))


    def wrong_answer(self):
        user_answer='false'
        self.give_feedback(self.quiz_brain.check_answer(user_answer))


    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)



