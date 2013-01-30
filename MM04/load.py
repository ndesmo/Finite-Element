import numpy as np
from scipy.integrate import dblquad

class load(object):
    def __init__(self):
        self.i=0
        
        def gfun(x):
            return 0.
        
        def hfun(x):
            return 1-x
        
        self.L = np.zeros(6)
        
        for i in range(6):
            self.i = i
            self.L[i] = dblquad(self.f,0,1,gfun,hfun)[0]
        print self.L
        

    def f(self, x, y):
        i = self.i
        def N(x, y, i=0):
            if i==0:
                v = (1-x-y)*(1-2*x-2*y)
            if i==1:
                v = x*(2*x-1)
            if i==2:
                v = y*(2*y-1)
            if i==3:
                v = 4*x*(1-x-y)
            if i==4:
                v = 4*x*y
            if i==5:
                v = 4*y*(1-x-y)
            return v
    
        def det(x,y):
            return 1+2*(np.sqrt(2)-1)*(x+y)
        
        def l(x,y,i):
            return -N(x,y,i)*det(x,y)
            
        F = l(x,y,i)
        return F

load()

