class Shop:
    def __init__(self,Name,Ma_d,Situated) -> None:
        self.Name = Name
        self.Ma_d = Ma_d
        self.situated = Situated

    def __repr__(self) -> str:
        return f"My Shop Name is {self.Name}. It manufracture by {self.Ma_d} and it's situated in {self.situated}"


class  Product:
    def __init__(self,name, manu, expi, origin) -> None:
        self.name = name
        self.manufracture_date = manu
        self.expire_date = expi
        self.origin = origin

    def __repr__(self) -> str:
        return f"My Product name is {self.name}. It manufracture date {self.manufracture_date} and expire date {self.expire_date}. It origin is {self.origin}"


mySHOp = Shop("SuperShop","Arc. SomeOne","Dhaka")
print(mySHOp)

myPRODUCT = Product("Hulululu",'08-11-16','08-11-26',"Bangladesh")
print(myPRODUCT)