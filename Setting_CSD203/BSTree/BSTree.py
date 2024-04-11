from Queue import *
from Node import *


class BSTree:
    def __init__(self, root=None):
        self.root = root

    def isEmpty(self):
        return self.root is None;

     
    def depth(self,p):
        count=0
        i=self.root
        while i:
            if i.data==p.data:
                return count
            elif i.data>p.data:
                i=i.left
            else :
                i=i.right
            count+=1
        return 0
    def max(self,a,b):
        if a>b:
            return a
        return b
    def height(self,p):
        if self.getNumofChildren(p)==0:
            return 0
        elif self.getNumofChildren(p)==-1:
            return 1+ self.height(p.left)
        elif self.getNumofChildren(p)==1:
            return 1+self.height(p.right)
        else:
            return  1+ self.max(self.height(p.left),self.height(p.right))
    def visit(self, nodex):
        print(nodex.data, end=' ')
    def insert(self,name, price):
        newNode = Node(data = Car(name, price))
        if name[0] == "B" or  price > 100:
        # Sửa điều kiện theo đề bài yêu cầu
            return
        if self.root is None:
            self.root = newNode
        else:
            current = self.root
            while current:
                if price < current.data.Price:
                    if current.left:
                        current = current.left
                    else:
                        current.left = newNode
                    
                        break
                elif price > current.data.Price:
                    if current.right:
                        current = current.right
                    else:
                        current.right = newNode
                        
                        break
                else:
                     break
    def pre_order(self, p):
        if p:
            self.visit(p)
            self.pre_order(p.left)
            self.pre_order(p.right)

    def inOrder(self, p):
        if p:
            self.inOrder(p.left)
            self.visit(p)
            self.inOrder(p.right)

    def postOrder(self, p):
        if p:
            self.postOrder(p.left)
            self.postOrder(p.right)
            self.visit(p)

    def addNode(self, x):
        nodeX = Node(x)
        if self.isEmpty():
            self.root = nodeX
        else:
            i = self.root
            par = i
            while i:
                par = i
                if i.data == x:
                    return
                if i.data > x:
                    i = i.left
                else:
                    i = i.right
            if par.data > x:
                par.left = nodeX
            else:
                par.right = nodeX

    def breadFirst(self):
        q = Queue()
        q.enqueue(self.root)
        while not q.isEmpty():
            r = q.dequeue()
            if r.left is not None:
                q.enqueue(r.left)
            if r.right is not None:
                q.enqueue(r.right)
            self.visit(r)
    def getNumofNode(self,p):
        if not p:
            return 0
        count=0
        q = Queue()
        q.enqueue(p)
        while not q.isEmpty():
            r = q.dequeue()
            if r.left is not None:
                q.enqueue(r.left)
            if r.right is not None:
                q.enqueue(r.right)
            #self.visit(r)
            count+=1
        return count
    def getNode(self, x):
        i = self.root
        while i:
            if i.data == x:
                return i
            if i.data > x:
                i = i.left
            else:
                i = i.right
        return None

    def getPar(self, p):
        i = self.root
        while i:
            if i.left == p or i.right == p:
                return i
            if i.data > p.data:
                i = i.left
            else:
                i = i.right
        return None


    def getRightMost(self, p):
        rm = p
        while rm.right :
            rm = rm.right
        return rm
    def getNumofChildren(self, p):
        if p.left is None and p.right is None:
            return 0
        elif p.left is None and p.right is not None:
            return 1
        elif p.left is not None and p.right is None:
            return -1
        else:
            return 2
    def deleteByCopy(self,p):
        if p is None :
            return
        if p==self.root:
            if self.getNumofChildren(p)==0:
                self.root=None
            elif self.getNumofChildren(p)==-1:
                self.root=self.root.left
            elif self.getNumofChildren(p)==1:
                self.root=self.root.right
            else :
                rm = self.getRightMost(p.left)
                parrm=self.getPar(rm)
                if parrm.left==rm:
                    parrm.left=rm.left
                else:
                    parrm.right=rm.left
                p.data=rm.data
        else: #xoa node p khong phai la root
            par=self.getPar(p)
            
            if self.getNumofChildren(p)==0:
                if par.left==p:
                    par.left=None
                else:
                    par.right=None
            elif self.getNumofChildren(p)==-1:
                if par.left==p:
                    par.left = p.left
                else:
                    par.right=p.left
            elif self.getNumofChildren(p)==1:
                if par.left==p:
                    par.left=p.right
                else:
                    par.right=p.right
            else:
                rm = self.getRightMost(p.left)
                parrm=self.getPar(rm)
                p.data=rm.data
                if parrm.left==rm:
                    parrm.left=rm.left
                else:
                    parrm.right=rm.left
                
#         if self.getNumofChildren(p)==0:
            
    def deleteByMerging(self, p):
        if p==self.root:
            if self.getNumofChildren(p)==0:
                self.root = None
            elif self.getNumofChildren(p)==-1:
                self.root = self.root.left
            elif self.getNumofChildren(p)==1:
                self.root = self.root.right
            else:
                rm=self.getRightMost(p.left)
                rm.right = p.right
                self.root = self.root.left
        else  : #khong phai node root
            par=self.getPar(p)
            if self.getNumofChildren(p)==-1:
                if par.left==p:
                    par.left = p.left
                else:
                    par.right = p.left
            elif self.getNumofChildren(p)==0:
                if par.left==p:
                    par.left = None
                else:
                    par.right = None
            elif self.getNumofChildren(p)==1:
                if par.left==p:
                    par.left = p.right
                else:
                    par.right = p.right
            else:#node p co 2 con
                rm=self.getRightMost(p.left)
                rm.right = p.right
                if par.left==p:
                    par.left = p.left
                else:
                    par.right = p.left

        pass
    def RightRotate(self,p):
        q=p.left
        p.left=q.right
        q.right=p
        if p==self.root:
            self.root=q;
        else:
            par=self.getPar(p)
            if par.left==p:
                par.left=q
            else:
                par.right=q
    def LeftRotate(self,p):
        q=p.left
        p.right=q.left
        q.left=p
        if p==self.root:
            self.root=q;
        else:
            par=self.getPar(p)
            if par.left==p:
                par.left=q
            else:
                par.right=q    
    def LR(self,p):
        if p is None:
            return None 
        q=p.right
        p.right=q.left
        q.left=p
        return q
    def LRx(self,x):
        nodex=self.getNode(x)
        par=self.getPar(nodex)
        if self.root==nodex:
            self.root = self.LR(nodex)        
        elif par.left==nodex:
            par.left=self.LR(nodex)
        else:
            par.right=self.LR(nodex)
    def RR(self, p):
        if p is None:
            return None
        q = p.left
        p.left = q.right
        q.right = p
        return q

    def RRx(self, x):
        nodex=self.getNode(x)
        par=self.getPar(nodex)
        if self.root==nodex:
            self.root = self.RR(nodex)        
        elif par.left==nodex:
            par.left=self.RR(nodex)
        else:
            par.right=self.RR(nodex) 
    def LRR(self, p):
        p.left = self.LR(p.left)
        return self.RR(p)
    def RLR(self, p):
        p.right=self.RR(p.right)
        return  self.LR(p)

    def LRRx(self, x):
        nodex = self.getNode(x)
        par = self.getPar(nodex)
        if self.root == nodex:
            self.root = self.LRR(nodex)
        elif par.left == nodex:
            par.left = self.LRR(nodex)
        else:
            par.right = self.LRR(nodex)

    def RLRx(self, x):
        nodex = self.getNode(x)
        par = self.getPar(nodex)
        if self.root == nodex:
            self.root = self.RLR(nodex)
        elif par.left == nodex:
            par.left = self.RLR(nodex)
        else:
            par.right = self.RLR(nodex)
   

        
    
        
        
        
        
        
        
        
        
        
        
        
