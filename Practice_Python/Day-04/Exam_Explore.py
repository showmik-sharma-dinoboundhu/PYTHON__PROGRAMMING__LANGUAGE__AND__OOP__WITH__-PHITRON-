class Exam:
    def __init__(self,examiner):
        self.examnier = examiner

    def Fee(self,taka):
        self.taka = taka
        taka = 500
        if self.taka >= 500:
            print("Qualified")
        
        else:
            print("Not Qualified")

myExam = Exam(1500)
myExam.Fee(500)