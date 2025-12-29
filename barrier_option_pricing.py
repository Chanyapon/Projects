import numpy as np

S0 = 100
K = 100
T = 1
H = 125
r = 0.06
N = 3
u = 1.1
d = 1/u
opttype = 'C'

def barrier_tree_slow(K,T,S0,H,r,N,u,d,opttype='C'):
    #precompute values
    dt = T/N
    q = (np.exp(r*dt)-u)/(u-d)
    disc = np.exp(-r*dt)
    
    # initialise asset prices at maturity - Time step N
    S = np.zeros(N+1)
    for j in range(0,N+1):
        S[j] = S[0] * u**j * d**(N-j)
        
    
    # initialise option values at maturity
    C = np.zeros(N+1)
    for j in range(0,N+1):
        if opttype == 'C':
            C[j] = max(0,S[j]-K)
        else:
            C[j] = max(0,K-S[j])
            
     # check terminal condition payoff
    for j in range(0,N+1):
        S = S0 * u**j * d**(N-j)
        if S >=H:
            C[j] = 0

    # step backwards through tree
    for i in np.arange(N-1,-1,-1):
        for j in range(0,i+1):
            S = S0*u**j*d**(N-j)
            if S>=H:
                C[j] = 0
            else:
                C[j] = disc*(q*C[j+1]+(1-q)*C[j])
    return C[0]

barrier_tree_slow(K,T,S0,H,r,N,u,d,opttype='C')
