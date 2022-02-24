# class Person:
#     def __init__(self,yas,kilo):

#         self.yas=yas
#         self.kilo=kilo
#     #methods
#     def intro(self):
#         print("Hello there" + (self.yas))    

#     def dt(self):

#         return 2022- self.yas
        

# p1=Person(yas=25,kilo=70)
# p2=Person("30","92")        
# p1.intro()

# print(f"yasım: {p1.yas} ve dogumtarihim: {p1.dt()}")


class Circle:
    pi= 3.14

    def __init__(self,yaricap=1):
        self.yaricap=yaricap


    #methods 
    def cevre(self):
        return 2*self.pi*self.yaricap

    def alan(self):
        return self.pi*(self.yaricap**2)

c1=Circle(5)
c2=Circle()

print(f"c1 alan: {c1.alan()}")
print(f"c2 cevre: {c2.cevre()}")