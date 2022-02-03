

'''
 "target1": { --------------------------------------------------"target2": {
       rate: 1.9                                                        rate: 2.8
       score_coordinate: [("x", 10), ("y", 12), ("z", 9)]               score_coordinate: [("x", 12), ("y", 89), ("z", 76)]
 }                                                                }                                  
     |
     |
     |
     |
     |

     "target3": {
       rate: 1.8                                                      
       score_coordinate: [("x", 12), ("y", 89), ("z", 12)]
    }

    Vertices= {"target1", "target2", "target3"}

    Edges = {("target1, "target2"), ("target1", "target3")]

    Given the list of target nodes as vertices and form a graph. 

'''

class ComputeGraph:
    def __init__(self, dicto=None):
        if dicto is None:
            dicto = {}
        self.dicto = dicto


    def getVertices_keys(self):
        vertices_storeKeys = []
        for vertex in self.dicto:
            vertices_storeKeys.append(vertex)
        return vertices_storeKeys

    def getVertices_names(self):
        vertices_storeNames = []
        for vertex in self.dicto:
            names = self.dicto[vertex][0]['name']
            vertices_storeNames.append(names)
        return vertices_storeNames

    


target1 = {
    "name": "target1", 
    "rate": 1.9, 
    "score_coordinate": [("x", 10), ("y", 12), ("z", 9)] 
}

target2 = {
    "name": "target2", 
    "rate": 2.8, 
    "score_coordinate": [("x", 12), ("y", 89), ("z", 76)] 
}

target3 = {
    "name": "target3", 
    "rate": 1.8, 
    "score_coordinate": [("x", 12), ("y", 89), ("z", 12)]
}


graph = {
    1: [target1, target2],
    2: [target2, target1],
    3: [target1, target3] 
}

graphing = ComputeGraph(graph)

print("Vertices: ", graphing.getVertices_keys())

print("Vertices Names: ", graphing.getVertices_names()) 





    


