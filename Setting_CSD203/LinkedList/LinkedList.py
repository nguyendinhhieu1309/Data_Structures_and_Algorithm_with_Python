from Node import *
class LinkedList:
    def __init__(self,head=None,tail=None ):
        self.head=head
        self.tail=tail
    def isEmpty(self):
        return self.head is None
    def addHead(self,x):
        nodeX = Node(x)
        if self.isEmpty():
            self.head=nodeX
            self.tail=nodeX
        else:
            nodeX.next=self.head
            self.head=nodeX
    def addTail(self,x):
        nodeX = Node(x)
        if self.isEmpty():
            self.head=nodeX;
            self.tail=nodeX;
        else:
            self.tail.next=nodeX;
            self.tail=nodeX;
    def size(self):
        #tra ve so node cua ds
        count=0
        p=self.head
        while p:
            count+=1
            p=p.next
        return count
    def getNode(self,pos):
        count=0
        p=self.head
        while p:
            if count==pos:
                return p
            p=p.next
            count+=1
        return None;
    def insrertAt(self,x,pos):
        nodeX=Node(x)
        if pos<0 or pos > self.size():
            return
        if pos==0:
            self.addHead(x)
        elif pos==self.size():
            self.addTail(x)
        else :
            p=self.getNode(pos-1)
            nodeX.next=p.next
            p.next=nodeX
        pass
    #them, xoa, sua, tim kiem, sap xep, thong ke
    #reuse
    def findMax(self):
        #tra ve gia tri lon nhat cua ds
        max=self.head.info
        p=self.head
        while p:
            if p.info>max:
                max=p.info
            p=p.next
        return max;
    def findMin(self):
    #tra ve gia tri nho nhat cua ds
        max=self.head.info
        p=self.head
        while p:
            if p.info<max:
                max=p.info
            p=p.next
        return max;
    def findx(self,x,nth):
        count=0
        ind=0
        p=self.head
        while p:
            if p.info==x:
                count+=1
            if count==nth:
                return ind
            p=p.next
            ind+=1
        return -999
    def removeFirst(self):
        if self.isEmpty():
            return
        self.head=self.head.next
    def removeLast(self):
        self.tail=self.getNode(self.size()-2)
        self.tail.next=None
        
    def removeAt(self,pos):
        if pos<0 or pos>=self.size():
            return
        if pos==0:
            self.removeFirst();
        elif pos==self.size()-1:
            self.removeLast();
        else:
            p=self.getNode(pos-1)
            p.next=p.next.next        
    def traverse(self):
        p=self.head
        while p:
            print(p.info,end=' ')
            p=p.next
        print()
    def swap(self,Node1,Node2):
        if Node1==None  or Node2 == None:
            return;
        tmp=Node1.info
        Node1.info=Node2.info
        Node2.info=tmp
    def sort(self,fromnode=None ,toNode=None):
        i=self.head
        while i:
            min=i;
            j=i.next
            while j:
                if j.info < min.info:
                    min=j;
                j=j.next
            if min!=i:
                self.swap(i,min)
            i=i.next
    def countx(self,x):
        count=0
        i=self.head
        while i:
            if i.info==x:
                count+=1
            i=i.next
        return  count
  
    def findLastMax(self):
        max=self.head.info
        i=self.head
        pos=0
        ind=0
        while i:
            if i.info>=max:
                max=i.info;
                pos=ind
            i=i.next
            ind+=1
        return pos
    
    def findFirstMax(self):
        max=self.head.info
        i=self.head
        pos=0
        ind=0
        while i:
            if i.info>max:
                max=i.info;
                pos=ind
            i=i.next
            ind+=1
        return pos


    def findLastMin(self):
        max=self.head.info
        i=self.head
        pos=0
        ind=0
        while i:
            if i.info<=max:
                max=i.info;
                pos=ind
            i=i.next
            ind+=1
        return pos
    def findFirstMin(self):
        max=self.head.info
        i=self.head
        pos=0
        ind=0
        while i:
            if i.info<max:
                max=i.info;
                pos=ind
            i=i.next
            ind+=1
        return pos
        
               
            
            
            
        
        
        
        
        