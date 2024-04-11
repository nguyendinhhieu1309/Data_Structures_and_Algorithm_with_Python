class Node:
    def __init__(self,x):
        self.data=x
        self.next=None     
        pass
class Queue:
    def __init__(self,head=None ,tail=None ):
        self.head=head
        self.tail=tail 
        pass
    def isEmpty(self):
        return self.head is None
        
    def enqueue(self,x):
        if not self.head:            
            self.head=Node(x)
            self.tail=self.head
        else:
            nodex=Node(x)
            self.tail.next=nodex
            self.tail=self.tail.next
    def dequeue(self):
        x=self.head.data
        self.head=self.head.next
        return x
class Graph:
    def __init__(self,data):
        self.adj=data
        self.V='ABCDEFGHIJKLMNOPQRST'
        pass
#      void breadth(boolean [] en, int i, RandomAccessFile f) throws Exception
#    {Queue q = new Queue();
#     int r,j;
#     q.enqueue(i); en[i]=true;
#     while(!q.isEmpty())
#      {r = q.dequeue();
#       fvisit(r,f);
#       for(j=0;j<n;j++)
#        {if(!en[j] && a[r][j]>0) {q.enqueue(j);en[j]=true;}
#        }
#      }
#    }
# 
#   void breadth(int  k, RandomAccessFile f) throws Exception
#    {boolean [] en = new boolean[20];
#     int i;
#     for(i=0;i<n;i++) en[i]=false;
#     breadth(en,k,f);
#     for(i=0;i<n;i++) if(!en[i]) breadth(en,i,f);
#    }
#    
    def bread(self,k,b):
        q=Queue()
        q.enqueue(k)
        b[k]=True 
        while not q.isEmpty():
            r=q.dequeue()
            print("%c, "%self.V[r],end=' ')
            for i in range(len(b)):
                if not b[i] and self.adj[r][i]>0:
                    q.enqueue(i)
                    b[i]=True 
        pass
    def breadFirst(self,k):
        b=[False]*len(self.adj)
        self.bread(k,b)
        for i in range(len(b)):
            if not b[i]:
                self.bread(i,b)
        pass
    def DepthFirst(self,start_V):
        b=[False]*len(self.adj)
        b[start_V]=True
        self.Depth(start_V,b)
        for i in range(len(b)):
            if not b[i]:
                b[i]=True
                self.Depth(i,b)
                       
        pass
    def Depth(self,start,b):
        print("%c "%self.V[start],end=' ')
        for i in range(0,len(b)):
            if self.adj[start][i]>0 and not b[i]:
                b[i]=True
                self.Depth(i,b)
        pass
    
    
#   void dijstra(int u, int v1,RandomAccessFile  f) throws IOException {
    def dijstra(self,u,v):
        inf=999 #gia tri vo cung
        dis=[-1]*len(self.adj)
        path=[-1]*len(self.adj)
        selected=[False ]*len(self.adj)
        sel=u        
        print()
        for i in range(0,len(dis)):
            dis[i]=self.adj[sel][i]
            path[i]=sel
        
        selected[sel]=True
        for k in range(0,len(self.adj)):
            min=inf
            for i in range(0,len(self.adj)):
                if not selected[i] and dis[i] < min:
                    
                    min=dis[i]
                    sel=i
                    print("%d "%min,end=' ')
            selected[sel]=True        
            for i in range(0,len(self.adj)):
                if not selected[i] and dis[i]> dis[sel]+self.adj[sel][i]:
                    dis[i]=dis[sel]+self.adj[sel][i]
                    path[i]=sel
                
                
        i=v
        s=""
        s1=""
        while (i!=u):
            s=self.V[i]+"("+str(dis[i])+") " +s
            s1=str(dis[i])+" "+s1
            i=path[i]
        s=self.V[u]+"("+str(dis[i])+") " +s
        s1=str(dis[u])+" "+s1
        
        print()
        print("%s \n%s"%(s,s1))
#         print('Quang duong di tu %s den %s la %d'%(self.V[u],self.V[v],dis[v]))
        print('%s-->%s:%d'%(self.V[u],self.V[v],dis[v]))
    def dijstra2(self,u,v):
        inf=999 #gia tri vo cung
        dis=[-1]*len(self.adj)
        path=[-1]*len(self.adj)
        selected=[False ]*len(self.adj)
        sel=u        
        print()
        for i in range(0,len(dis)):
            dis[i]=self.adj[sel][i]
            path[i]=sel
        
        selected[sel]=True
        for k in range(0,len(self.adj)):
            min=inf
            for i in range(0,len(self.adj)):
                if not selected[i] and dis[i] < min:
                    
                    min=dis[i]
                    sel=i
                    #print("%d "%min,end=' ')
            selected[sel]=True        
            for i in range(0,len(self.adj)):
                if not selected[i] and dis[i]> dis[sel]+self.adj[sel][i]:
                    dis[i]=dis[sel]+self.adj[sel][i]
                    path[i]=sel
                
                
        i=v
        s=""
        s1=""
        while (i!=u):
            s=self.V[i]+"-"+str(dis[i])+"" +s
            s1=str(dis[i])+" "+s1
            i=path[i]
        s=self.V[u]+"-"+str(dis[i])+" " +s
        s1=str(dis[u])+" "+s1
        
        print()
        print("%s \n%s"%(s,s1))
#         print('Quang duong di tu %s den %s la %d'%(self.V[u],self.V[v],dis[v]))
        print('%s->%s:%d'%(self.V[u],self.V[v],dis[v]))
    def deg(self,v):
        count=0;
        for i in range(len(self.adj)):
            count+=self.adj[v][i];
        return count;
    def isolated(self,k):
        if self.deg(k)==0:
            return True
        return  False 
    def Euler(self,X):
        S=Stack()
        E=[]
        S.push(X)
        while   not S.isEmpty():
            r = S.top()
            if self.isolated(r):
                S.pop()
                E.append(chr(r+65))
            else :
               for Y in range(0,len(self.a)):
                   if self.a[r][Y]>0:
                       break
               S.push(Y)
               self.a[r][Y]-=1;
               self.a[Y][r]-=1
        str=""
        for i in range(0,len(E)-1):
            str=str+E[i]+","
        str=str+E[len(E)-1]
        print(str)
        
# https://drive.google.com/open?id=1kRy_MTzPKICKKR_6MBX3IR9bEuggIviP&usp=drive_fs
            # A  B  C  D  E  F  G  H  I
adj=[       [0, 0, 0, 0, 1, 1, 1, 0, 1], #A
            [0, 0, 0, 0, 0, 0, 1, 0, 0], #B
            [0, 0, 0, 0, 0, 0, 0, 1, 0], #C
            [0, 0, 0, 0, 0, 0, 0, 1, 0], #D
            [1, 0, 0, 0, 0, 1, 0, 0, 1], #E
            [1, 0, 0, 0, 1, 0, 0, 0, 1], #F
            [1, 1, 0, 0, 0, 0, 0, 0, 0], #G
            [0, 0, 1, 1, 0, 0, 0, 0, 0], #H
            [1, 0, 0, 0, 1, 1, 0, 0, 0]  #I
        ]
# https://drive.google.com/open?id=1kYr-FLL4-aArQpyIvgpnYijx-tEDEn_x&usp=drive_fs
# A       B     C      D      E      F   
adj1=[
   [0 ,   7  ,  9  , 999  , 999   , 14  ], #A
   [7,    0 ,  10 ,   15  , 999   ,999  ], #B
   [9 ,  10  ,  0  ,  11  , 999  ,   2  ], #C
   [999, 15,   11 ,   0   ,  6,    999  ], #D
   [999, 999 ,999  , 6  ,   0  ,    9  ], #E
   [14  ,999 ,  2  , 999 ,  9 ,      0]  #F
  ]
# print("\nDepth first")   
g = Graph(adj1)
# g.DepthFirst(7)
# print("\ndeg of A:%d"%g.deg(1))
# print("\nBread first")
# g.breadFirst(7)
g.dijstra2(2,5)