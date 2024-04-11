from  Node import *
class  Stack :
    def __init__(self,top=None):
        self.top=top
    def isEmpty(self):
        return  self.top is None
    def addHead(self,x):
        nodeX = Node(x)
        if self.isEmpty():
            self.top=nodeX
        else:
            nodeX.next=self.top
            self.top=nodeX
    def push(self,x):
        self.addHead(x)
        pass
    def pop(self):
        x =self.top.data
        self.top=self.top.next
        return x
    