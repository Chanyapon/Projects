"""
Binomail Tree Representation
Stock tree can be represented using nodes (i,j) and intial stock price S0
S[i,j] = S0*(u**j)*(d**(i-j))
C[i,j] represents contract price at each node (i,j). Where C[N,j] represents final payoff function that we can define.
For this tutorial will price a European Call, so C[N,j] = Max(S[N,j]-K,0)

"""
import numpy as np

S0 = 100
K = 100
T = 1
r = 0.06
N = 3
u = 1.1
d = 1/u
opttype = 'C'

def binomial_tree_slow(K,T,S0,r,N,u,d,opttype='C'):
    #precommute constants
    dt = T/N
    q = (np.exp(r*dt)-d)/(u-d)
    disc = np.exp(-r*dt)
    
    # initialise asset prices at maturity - Time step N
    S = np.zeros(N+1)
    S[0] = S0*d**N
    for j in range(1,N+1):
        S[j] = S[j-1]*u/d
        
    # initialise option values at maturity
    C = np.zeros(N+1)
    for j in range(0,N+1):
        C[j] = max(0,S[j]-K)
        
    # step backwards through tree
    for i in np.arange(N,0,-1):
        for j in range(0,i):
            C[j] = disc * (q*C[j+1] + (1-q)*C[j])
            
    return C[0]

binomial_tree_slow(K,T,S0,r,N,u,d,opttype='C')

def binomial_tree_fast(K,T,S0,r,N,u,d,opttype='C'):
    #precommute constants
    dt = T/N
    q = (np.exp(r*dt)-d)/(u-d)
    disc = np.exp(-r*dt)
    
    # initialise asset prices at maturity - Time step N
    C = S0*d**(np.arange(N,-1,-1))*u**(np.arange(0,N+1,1))
    
    # initialise option values at maturity
    
    C = np.maximum(C-K,np.zeros(N+1))
        
    # step backwards through tree
    for i in np.arange(N,0,-1):
        C = disc * (q*C[1:i+1] + (1-q)*C[0:i])
        
    return C[0]

binomial_tree_fast(K,T,S0,r,N,u,d,opttype='C')
