#class
class Person:

#class attributes
    address="no information"
  

#constructor(yapıcı metod)

    def __init__(self,name,year):
        self.name=name
        self.year=year
        print("init metodu calisti")

#object,(instance)

p1 = Person("ali",1990)
p2 = Person("hsyn",1995)


