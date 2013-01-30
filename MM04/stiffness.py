import numpy as np
from scipy.integrate import dblquad

class stiffness(object):
    def __init__(self):
        self.i=0
        self.j=0
        
        def gfun(x):
            return 0.
        
        def hfun(x):
            return 1-x
        
        self.K = np.zeros((6,6))
        
        for i in range(6):
            self.i = i
            for j in range(6):
                self.j = j
                self.K[i,j] = dblquad(self.f,0,1,gfun,hfun)[0]
        print self.K
        
        rowzero = True
        for i in range(6):
            s = 0
            for j in range(6):
                s += self.K[i,j]
            if np.abs(s)>1e-4:
                rowzero = False
                print "Failed at row "+str(i)+". Got sum = "+str(s)
        if rowzero: print "Rows sum to zero"
        
        symmetric = True        
        for i in range(6):
            for j in range(i,6):
                if np.abs(self.K[i,j]-self.K[j,i]) > 1e-4:
                    symmetric = False
                    print "Not symmetric for K"+str(i)+str(j)
        if symmetric: print "Symmetric"
        

    def f(self, x, y):
        i = self.i ; j = self.j
        def dNdx(x, y, i=0):
            if i==0:
                v = -3+4*x+4*y
            if i==1:
                v = 4*x-1
            if i==2:
                v = 0
            if i==3:
                v = 4-8*x-4*y
            if i==4:
                v = 4*y
            if i==5:
                v = -4*y
            return v
    
        def dNdy(x, y, i=0):
            if i==0:
                v = -3+4*x+4*y
            if i==1:
                v = 0
            if i==2:
                v = 4*y-1
            if i==3:
                v = -4*x
            if i==4:
                v = 4*x
            if i==5:
                v = 4-8*y-4*x
            return v
        
        def dxdx(x,y):
            return 1+2*(np.sqrt(2)-1)*y
        def dxdy(x,y):
            return 2*(np.sqrt(2)-1)*x
        def dydx(x,y):
            return 2*(np.sqrt(2)-1)*y
        def dydy(x,y):
            return 1+2*(np.sqrt(2)-1)*x
        
        def J(x,y):
            return np.array([[dxdx(x,y),dxdy(x,y)],[dydx(x,y),dydy(x,y)]])
        
        def det(x,y):
            #return dxdx(x,y)*dydy(x,y)-dxdy(x,y)*dydx(x,y)
            return 1+2*(np.sqrt(2)-1)*(x+y)
        
        def iJ(x,y):
            return 1/det(x,y)*np.array([[dydy(x,y),-dxdy(x,y)],[-dydx(x,y),dxdx(x,y)]])
        
        def iJT(x,y):
            return np.array([[dydy(x,y),-dydx(x,y)],[-dxdy(x,y),dxdx(x,y)]])
        
        def row(x,y,i):
            return np.array([dNdx(x,y,i), dNdy(x,y,i)])
        
        def col(x,y,j):
            return np.array([[dNdx(x,y,j)], [dNdy(x,y,j)]])
        
        def k(x,y,i,j):
            return np.dot(row(x,y,i),np.dot(iJ(x,y),np.dot(np.identity(2),np.dot(iJT(x,y),col(x,y,j)))))
        
            
        F = k(x,y,i,j)
        return F

stiffness()

