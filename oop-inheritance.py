#inheritance (kalıtım): miras alma

#Person => name, lastname, age, eat(), run(), drink()
#Student(Person), Teacher(Person)


class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        print(" person created  ")

    def who_am_i(self):
        print("ı am a person")

    def eat(self):
        print("ı am eating")

  
class Teacher(Person):
    def __init__(self,fname,lname,number):

    
        self.numara=number
        Person.__init__(self,fname,lname)
        print("teacher created")
p1=Person("hsyn","uyanik")
s1=Teacher("ali","veli",123)


print(p1.firstname + " " + p1.lastname)
print(s1.firstname + " " +  s1.lastname + " " + str(s1.numara))
