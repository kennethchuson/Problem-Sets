

class Mom:

    def __init__(self, ethnicity):
        self.ethnicity = ethnicity
        print("race: ", self.ethnicity) 

    def who(self):
        print("Mom")

    def define(self):
        print("working") 
        
        


class Child_One(Mom):

    def __init__(self, ethnicity):
        Mom.__init__(self, ethnicity)

    def get_ethnicity():
        print("child one race: ", self.ethnicity)


    def who(self):
        print("child one")

    def define(self):
        print("playing cars") 
    
    

class Child_Two(Mom):

    def __init__(self, ethnicity):
        Mom.__init__(self, ethnicity)

    def get_ethnicity():
        print("child two race: ", self.ethnicity)

    def who(self):
        print("child two")

    def define(self):
        print("playing trucks")



a = Mom("American")
b = Child_One("Chinese")
c = Child_Two("half American half Chinese") 

print(" ---  mom ---- ") 
print(a.who())
print(a.define())
print(" -- child one -- ")
print(b.who())
print(b.define()) 

print(" -- child two -- ")
print(c.who())
print(c.define()) 






    

    
