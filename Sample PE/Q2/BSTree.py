from Car import *
from Node import *
class NodeQ:
    def __init__(self,data):
        self.data = data
        self.next = None
class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head ==None
    def EnQueue(self, data):
        node = NodeQ(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    #end def
    def DeQueue(self):
        if self.isEmpty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data
#end class    
class BSTree:
    def __init__(self):
        self.root = None
    # end def
    def clear(self):
        self.root = None
    def isEmpty(self):
        return self.root == None
    #end def
    def insert(self,name, price):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
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
        
        #########################
       
    #end def
    def visit(self,p):
        if p==None:
            return
        print(f"{p.data}",end =" ")
    #end def
    def preOrder(self,p):
        if p==None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)
    #end def
    def preVisit(self):
        self.preOrder(self.root)
        print("")
    #end def
    def postOrder(self,p):
        if p==None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)
    #end def
    def postVisit(self):
        self.postOrder(self.root)
        print("")
    #end def
    def inOrder(self,p):
        if p==None:
            return
        self.inOrder(p.left)
        self.visit(p)
        self.inOrder(p.right)        
    #end def
    def inVisit(self):
        self.inOrder(self.root)
        print("")
    #end def
    def breadth_first(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            self.visit(p)
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        print("")        
    #end def
    def f2(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        self.preOrder2(self.root)
        print('')
    def preOrder2(self,p):
        if p==None:
            return
        if p.data.Price <= 5 and p.data.Price >= 3:
            self.visit(p)
        self.preOrder2(p.left)
        self.preOrder2(p.right)   


        ####################
        pass
    def f3(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        p = self.breadth_first2()
        self.deleteByCopy(p) #Nếu đề ko yêu cùng dùng left hay right thì thường là dùng left
        #self.delByMergingLeft(p)#Nếu đề ko yêu cùng dùng left hay right thì thường là dùng left
        
    
##############Delete by Copy                
    def getPar(self, p):
        i = self.root
        while i:
            if i.left == p or i.right == p:
                return i
            if i.data.Price > p.data.Price:
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
                p.data.Price=rm.data.Price
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
                p.data.Price=rm.data.Price
                if parrm.left==rm:
                    parrm.left=rm.left
                else:
                    parrm.right=rm.left
    def breadth_first2(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and p.right and p.data.Price < 7:
            # Đề yêu cầu là node thứ mấy thì count bằng bấy nhiêu (ví dụ đề yêu cầu 'first node' thì count = 1
                return p
            #self.visit(p)
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        print("")                
        #############################    
        pass
    def f4(self):
        #  ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        p=self.breadth_first3()
        self.rotate_right(p)
    def breadth_first3(self):
        if self.isEmpty():
            return
        my = MyQueue()
        my.EnQueue(self.root)
        while not my.isEmpty():
            p = my.DeQueue()
            if p.left and p.data.Price < 7:
                return p
            if p.left!=None:
                my.EnQueue(p.left)
            if p.right!=None:
                my.EnQueue(p.right)
        print("")

    def _find_parent(self,root,node):
        if not root:
            return None
        if root.left == node or root.right == node:             
            return root
        if node.data.Age < root.data.Age:
        #Sửa data. theo yêu cầu đề bài
            return self._find_parent(root.left, node)
        else:
            return self._find_parent(root.right, node)
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


        #################################
        pass


# end class
