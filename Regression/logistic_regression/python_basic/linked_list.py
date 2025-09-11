class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        obj = Node(data)
        if self.head == None:
            self.head = obj
            return
        curr_ptr = self.head
        while curr_ptr.next != None:
            curr_ptr = curr_ptr.next
        curr_ptr.next = obj   
            

    def showVal(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next




a = linkedlist()


a.addNode("b")
a.addNode("bc")
a.addNode("c")
a.addNode("bcd")

a.showVal()
