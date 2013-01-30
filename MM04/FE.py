import numpy as np
from load import load
from stiffness import stiffness
from numpy.linalg import solve

K = stiffness().K
L = load().L

k = np.array([[K[0,0],K[0,3],K[0,5]],[K[3,0],K[3,3],K[3,5]],[K[5,0],K[5,3],K[5,5]]])
l = np.array([[L[0]],[L[3]],[L[5]]])

z = solve(k,l)
print "Reduced problem deflections z1, z4 and z6 are"
print z

Z = np.array([z[0],0.,0.,z[1],0.,z[2]])
R = np.dot(K,Z) - L
print "Boundary vector:"
print R