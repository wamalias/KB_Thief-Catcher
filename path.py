 
class Branch (object) :  
    def __init__(self, index, heur):
        self.index = index
        self.heur = heur
        Nodes.append(self)

Nodes = []

def append(x, y, index):
    Branch(index, x+y)
    
    #for Node in Nodes :
    #    print(Node.index, Node.heur)
    #print("\n\n")
    
def check(path) :
    start = '#'
    for branch in Nodes :
        if(branch.index == path) :
            start = branch
            
    print(start.index, start.heur)
    
def map (level) :
    for row in level :
        for col in level :
            if col == 'Q' :
                print("perempatan")    