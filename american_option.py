"""
American Option Characteristics
Put Option

"""
import numpy as np

S0 = 100
K = 100
T = 1
r = 0.06
N = 3
u = 1.1
d = 1/u
opttype = 'P'

def american_slow_tree(K,T,S0,r,N,u,d,opttype='P'):
    #precompute values
    dt = T/N
    q = (np.exp(r*dt)-u)/(u-d)
    disc = np.exp(-r*dt)
    
    # initialise stock prices at maturity
    S = np.zeros(N+1)
    for j in range(0,N+1):
        S[j] = S[0]*u**j*d**(N-j)
        
    # option payoff
    C = np.zeros(N+1)
    for j in range(0,N+1):
        if opttype=='P':
            C[j] = max(0, K-S[j])
        else:
            C[j] = max(0, S[j]-K)
    
    #backwards recursion through the tree
    for i in np.arange(N-1,-1,-1):
        for j in range(0,i+1):
            S = S0*u**j*d**(i-j)
            C[j] = disc * (q*C[j+1]+(1-q)*C[j])
            if opttype=='P':
                C[j] = max(C[j], K-S)
            else:
                C[j] = max(C[j], S-K)
 
    return C[0]
american_slow_tree(K,T,S0,r,N,u,d,opttype='P')
