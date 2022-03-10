

class Test:

    name = ""
    age = 0

    def __init__(self, weight = 0.0, height = 0.0):
        self.weight = weight 
        self.height = height
       

    def get_weight(self):
        return self.weight


    def get_height(self):
        return self.height


t = Test(150.4, 5.9)
t.name = "Kailah"
t.age = 19
name = t.name
age = t.age
weight = t.get_weight()
height = t.get_height()

print("name: ",  name)
print("age: ", age)
print("weight: ", weight)
print("height: ", height) 
