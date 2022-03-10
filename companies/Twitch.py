




class Twitch(object):

    def __init__(self, arr):
        self.arr = arr
        
    def StreamerOnline(self, name, views, category):
        return self.arr.append((name, views, category)) 

    def UpdateViews(self, name, views, category):
    
        arr2 = [ list((n, v, c)) for (n, v, c) in self.arr ]
        res = [] 
        for i in range(len(arr2)):
            a = arr2[i][0]
            b = arr2[i][1]
            c = arr2[i][2]
            if a == name:
                b = views
            res.append((a, b, c))
            print(res) 
    

    def UpdateCategory(self, name, category, change_category):
        arr2 = [ list((n, v, c)) for (n, v, c) in self.arr ]
        res = [] 
        for i in range(len(arr2)):
            a = arr2[i][0]
            b = arr2[i][1]
            c = arr2[i][2]
            if c == category and a == name:
                c = change_category
            res.append((a, b, c))
            print(res) 


    
    def ViewsInCategory(self):
        category_list = []
        for (n, v, c) in self.arr:
            category_list.append(c)
        print(category_list) 

    def TopStreamerInCategory(self):
        top_c = ""
        m = 0 
        for (n, v, c) in self.arr:
            if m < v:
                top_c = c
        print(top_c) 

    def TopStreamer(self):
        top_n = ""
        m = 0 
        for (n, v, c) in self.arr:
            if m < v:
                top_n = n
        print(top_n)  
    
    def display(self):
        print(self.arr)




arr = [("Ninja", 1000, "Fortnite"), ("Pokimane", 40000, "Valorant")]




t = Twitch(arr)



t.StreamerOnline("StreamerOnline", 75000, "AOC")
print("added streamer: ") 
t.display()
print("update views") 
t.UpdateViews("Ninja", 120000, "Fortnite")
print("update category")
t.UpdateCategory("Ninja", "Fortnite", "Warzone")
print("category list")
t.ViewsInCategory()
print("Top Streamer in category")
t.TopStreamerInCategory()
print("Top Streamer")
t.TopStreamer() 


