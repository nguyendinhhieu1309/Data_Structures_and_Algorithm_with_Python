from  NodeQ import  *
class  Queue:
    def __init__(self,head=None,tail=None ):
        self.head=head
        self.tail=tail
    def isEmpty(self):
        return self.head is None
    def enqueue(self,x):
        nodex = NodeQ(x)
        if self.isEmpty():
            self.head=nodex
            self.tail=nodex
        else:
            self.tail.next=nodex
            self.tail=nodex            
        pass
    def dequeue(self):
        if self.isEmpty():
            return  None ;
        x=self.head.data
        self.head=self.head.next
        return x;
        pass
    