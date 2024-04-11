from Car import *
from Node import *
class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head ==None
    def traverse(self):
        pt = self.head
        while pt:
            print(pt.data, end = " ")
            pt = pt.next
        print("")        
    def clear(self):
        self.head = None
#Q1-1
    def addLast(self, name="", price=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        if name.startswith("B") or price >100:
            return
        n = Node(Car(name,price))
        if (self.isEmpty()):
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n                


        pass
    # end def
#Q1-2    
    def addFirst(self, name="", price=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        n = Node(Car(name,price))
        if self.isEmpty():
            self.head=n
            self.tail=n
        else:
            n.next=self.head
            self.head=n




        pass
    # end def
#Q1-3
    def delete(self, price =0):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        p=self.head
        while p.next:
            if p.next.data.Price==price:
                p.next=p.next.next
                return
            p=p.next
            



        pass 
    #end def
# Q1-4
    def sort(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        self.sortAsc()
    def swap(self,Node1,Node2):
        if Node1==None  or Node2 == None:
            return;
        tmp=Node1.data
        Node1.data=Node2.data
        Node2.data=tmp
    def sortAsc(self,fromnode=None ,toNode=None):
        i=self.head
        while i is not toNode:
            min=i;
            j=i.next
            while j is not toNode:
                if j.data.Price < min.data.Price:
                    min=j;
                j=j.next
            if min!=i:
                self.swap(i,min)
            i=i.next
    


        
        
    #end def    