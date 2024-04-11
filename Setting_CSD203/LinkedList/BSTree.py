from Queue import *
from Node import  *
class  BSTree:
    def __init__(self,root=None):
        self.root=root
    def isEmpty(self):
        return self.root is None ;
    def findNode(self,key):
        if self.isEmpty():
            return  None
        p=self.root
        while p:
            if p.data==key:
                return p
            elif p.data>key:
                p=p.left
            else:
                p=p.right
        return None
    def  findPar(self,nodex):
        if nodex is None :
            return  None 
        p=self.root
        par=None 
        while p:            
            if p==nodex:
                return par;
            par=p;
            if p.data>nodex.data:
                p=p.left
            else :
                p=p.right
        
        return None 
    
                
    def visit(self,nodex):
        print(nodex.data,end=' ')
        
    def pre_order(self,p):
        if  p:
            self.visit(p)
            self.pre_order(p.left)
            self.pre_order(p.right)
            
    def inOrder(self,p):
        if p:
            self.inOrder(p.left)
            self.visit(p)
            self.inOrder(p.right)
    def postOrder(self,p):
        if p:
            self.postOrder(p.left)
            self.postOrder(p.right)
            self.visit(p)
        
    def addNode(self,x):
        nodeX=Node(x)
        if self.isEmpty():
            self.root=nodeX
        else:
            i=self.root
            par=i
            while i:
                par=i
                if i.data==x:
                    return
                if i.data>x:
                    i=i.left
                else:
                    i=i.right
            if par.data>x:
                par.left=nodeX
            else:
                par.right=nodeX
            
    def rightMost(self,nodex):
        if nodex is None :
            return None
        p = nodex
        while p.right:
            p=p.right
        return p
    pass
    def numofchildren(self,nodex):
        if nodex is None:
            return;
        if nodex.left is None  and nodex.right is None :
            return 0;
        elif nodex.left == None and nodex.right is not None:
            return 1;
        elif nodex.left is not None  and nodex.right is None :
            return -1
        else :
            return 2
    def max1(self,a,b):
        if a>b:
            return  a
        else :
            return b;
    def height(self,nodex):
        if nodex is None :
            return 0
        if self.numofchildren(nodex)==0:
            return 0
        elif self.numofchildren(nodex)==-1:
            return 1+self.height(nodex.left)
        elif self.numofchildren(nodex)==1:
            return 1+self.height(nodex.right)       
   
        return self.max1(self.height(nodex.left),self.height(nodex.right))+1
    
    def deletebyMerging(self,key):
        nodekey = self.findNode(key)
        if nodekey is None:
            return 
        par=self.findPar(nodekey)
        if self.root.data==key:  
            if self.root.left==None:
                self.root=self.root.right
            else :
                rm=self.rightMost(self.root.left)
                rm.right=self.root.right
                self.root=self.root.left
        else:
            node_del=self.findNode(key)
            par=Node(0)
            #node can xoa la node la
            par=self.findPar(node_del)
            if self.numofchildren(node_del)==0:
                if par.left == node_del:
                    par.left = None
                else:
                    par.right=None
            elif  self.numofchildren(node_del)== -1: #node xoa chi co con trai
                if par.left==node_del:
                    par.left=node_del.left
                else:
                    par.right = node_del.left
            elif self.numofchildren(node_del)== 1: #node xoa chi co con phai
                if par.left==node_del:
                    par.left=node_del.right
                else:
                    par.right=node_del.right
            else : #node xoa co 2 con
                nodeRM=self.rightMost(node_del.left)
                nodeRM.right = node_del.right
                if par.left  == node_del:
                    par.left = node_del.left
                else:
                    par.right = node_del.left
    def deletebyCopy(self,key):
        node_key=self.findNode(key)
        par=self.findPar(node_key)
        if node_key is None :
            return
        if node_key==self.root and node_key.left is None:
            self.root=self.root.right
        else:
            if self.numofchildren(node_key)==0:
                if par.left==node_key:
                    par.left = None
                else :
                    par.right  =None
            elif self.numofchildren(node_key)==1:
                if par.left==node_key:
                    par.left = node_key.right
                else:
                    par.right=node_key.right
            else:                                   
                node_RM = self.rightMost(node_key.left)
                par = self.findPar(node_RM)
                node_key.data = node_RM.data
                if par.left == node_RM:
                    par.left = node_RM.left
                else:
                    par.right = node_RM.left
    def  test(self):
        print("\nTest Thony two windows");
        self.addNode(111)
        print( self.height(self.root))
    def tes2(self):
        print("test2");
        self.max1(3,4)
    def breadFirstOrder(self):
        q=Queue()
        q.enqueue(self.root)
        r = NodeQ()
        while not q.isEmpty():
            r = q.dequeue()
            if r.left is not None :
                q.enqueue(r.left)
            if r.right is not None :
                q.enqueue(r.right)
            self.visit(r)
    
    def f1(self):
        q=Queue()
        q.enqueue(self.root)
        r = NodeQ()
        while not q.isEmpty():
            r = q.dequeue()
            if r.left is not None :
                q.enqueue(r.left)
            if r.right is not None :
                q.enqueue(r.right)
            if r.left is not None and r.right is not None:
                self.visit(r)        
        
    def f2(self):
        q=Queue()
        q.enqueue(self.root)
        r = NodeQ()
        while not q.isEmpty():
            r = q.dequeue()
            if r.left is not None :
                q.enqueue(r.left)
            if r.right is not None :
                q.enqueue(r.right)
            if r.left is not None and r.right is not None and r.data<10:
                self.visit(r)
    count=0
    def inOrderf3(self,p):
        if p:
            self.inOrderf3(p.left)
            if p.left is not None  and p.right is not None and p.data<10:
                self.count+=1
                if self.count==2:
                    self.visit(p)
#                self.count+=1
            self.inOrderf3(p.right)
        
    def pre_orderF4(self,p):
        if  p:
            if p.left is not None or p.right is not None:
                self.count+=1
                if self.count==4:                    
                    self.visit(p)
            self.pre_orderF4(p.left)
            self.pre_orderF4(p.right)