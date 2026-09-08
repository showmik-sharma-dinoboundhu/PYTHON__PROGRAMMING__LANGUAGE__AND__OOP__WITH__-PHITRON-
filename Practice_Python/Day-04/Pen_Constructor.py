class Pen:
    Brand = "Matador"

    def __init__(self,Name,Owner,Ink,Price):
        self.Name = Name
        self.Owner = Owner
        self.Ink = Ink
        self.Price = Price

    
    def comments(self,message):
        text = f"My message is this to Matador: {message}"
        return text
    
allPen = Pen(Name="Matador",Owner="Matador Company",Ink="Normal Ink",Price=6)
print(Pen.Brand)

myPen = Pen("Matador Alltime","Matador Company","Normal Pen Ink",6)
print(myPen.Name,myPen.Owner,myPen.Ink,myPen.Price)

myComments = allPen
print(myComments.comments("Go Ahead Matador!!"))