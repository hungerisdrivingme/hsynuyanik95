
class Question:
    def __init__(self,text,choices,answer):

        self.text=text
        self.choices=choices
        self.answer=answer
    
    def checkanswer(self,answer):
        return self.answer==answer

        


q1=Question("en iyi programlama dili hangisidir?",["python","java","c","javascript"],"python")
q2=Question("en populer programlama dili hangisidir?",["python","java","c","javascript"],"java")
q3=Question("en karlı programlama dili hangisidir?",["python","java","c","javascript"],"c")
questions=[q1,q2,q3]

# print(q1.checkanswer("python"))
# print(q2.checkanswer("python"))
# print(q3.checkanswer("python"))


class Quiz:
    def __init__(self,questions):
        
        self.questions = questions
        self.score=0
        self.questionindex=0
    
    def getquestion(self):
        return self.questions[self.questionindex]

    def displayquestion(self):

        question= self.getquestion()

        print(f"soru {self.questionindex +1}:  {question.text} ")
        for q in question.choices:
            print("-"+q)

        answer= input("cevap: ")
        print(question.checkanswer(answer))



quiz=Quiz(questions)

quiz.displayquestion()

