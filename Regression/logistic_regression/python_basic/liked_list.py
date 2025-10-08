class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class linkedList:
    
    
    def __init__(self):
        self.root = None
        print("inside init")
    
    def addNode(self, data):
        #print("inside addNode")
        if self.root == None:
            #print("inside if")
            self.root = node(data)
        else:
            #print("inside next")
            pos = self.root
            while pos.next != None:
                pos = pos.next
            pos.next = node(data) 
            #print(f"added {data} at {pos.next}")
            #self.root.next = node(data)

    def showNodes(self):
        pos = self.root
        while pos:
            print(pos.data)
            pos = pos.next
            #break
        


l = linkedList()

l.addNode(12)
l.addNode(89)
l.addNode(32)
l.addNode(321)
l.addNode(342)
l.addNode(4)

l.showNodes()