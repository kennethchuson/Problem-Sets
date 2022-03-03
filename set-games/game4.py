



class Node_Direction(object):
    def __ini__(self, x, y):
        self.x = x
        self.y = y
        
    def Yuto_distance(self, iter_one, iter_two):
        a = 0 
        if self.x != self.y:
            a = (iter_one + self.x) * (iter_two + self.y)
            if self.x < self.y:
                a *= 2
            if self.y > self.x: 
                a -= pow(self.x, 2) 
        else:
            return -1
        return a 
        


class Graph(object):

    def __init__(self, graph, choose_one):
        self.graph = graph
        self.choose_one = choose_one

    def Far(self):
        res = []
        mapping = {}
        find_max = 0 
        for (key, val) in self.graph.items():
            for i in range(len(val)):
                identify_name = val[i][0] 
                identify_cost = val[i][1]
                mapping[identify_cost] = identify_name

            if key[0] == self.choose_one:
                cost_chose = key[2]
                for (key2, val2) in mapping.items():
                    adding_measure = cost_chose + key2
                    if adding_measure > find_max:
                        print(adding_measure) 
                        find_max = adding_measure
                        chose_name_closer = val2
                        res.append((find_max, chose_name_closer)) 
        return res

    def Total_mat(self):
        s = 0 
        for (key, val) in self.graph.items():
            for i in range(len(val)):
                s += val[i][1]
        return s 
                    
                    
    def Direction_mashed(self, x_give, y_give):
         get_far = self.Far()
         define = ""
         
         for (x, y) in get_far:
             direct_x = Node_Direction(x_give, y_give)
             direct_y = Node_Direction(x_give, y_give)
             a = direct_x.Yuto_distance(x, x + 1)
             b = direct_y.Yuto_distance(x + 1, x)
             if a == b:
                 define = "Smashed!"
             else:
                 define = "Missed!"
         return define
                
                 
         




universe_graph = {
    ("Test1", "A", 23): [
                            ["Test2", 40],
                            ["Test3", 11] 
                        
                        ],
    ("Test2", "B", 15): [
                            ["Test1", 87],
                            ["Test3", 19] 
                    
                        ],
    ("Test3", "C", 20): [
                            ["Test2", 11],
                            ["Test1", 41] 
                        ]
}

choose_one = "Test2" 
class_graph = Graph(universe_graph, choose_one)

a = class_graph.Far()
b = class_graph.Total_mat()
print("Far away for {}".format(choose_one), a)
print("Total values: ", b)




