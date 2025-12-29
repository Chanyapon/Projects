"""
Binomial Asset Pricing Model - Choosing Parameters.

Cox, Ross and Rubinstein (CRR)
Jarrow and Rudd (JR)
Equal probabilities (EQP)
Trigeorgis (TRG)
"""
import numpy as np

S0 = 100
K = 110
T = 0.5
r = 0.06
N = 100
sigma = 0.3 # Annualised stock price volatility 30%
opttype = 'C'

def CRR_method(K,T,S0,r,N,sigma,opttype='C'):
    #precommute constants
    dt = T/N
    u = np.exp(sigma*np.sqrt(dt))
    d = 1/u
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
CRR_method(K,T,S0,r,N,sigma,opttype='C')

def JR_method(K,T,S0,r,N,sigma,opttype='C'):
    #precommute constants
    dt = T/N
    nu = r - 0.5*sigma**2
    u = np.exp(nu*dt + sigma*np.sqrt(dt))
    d = np.exp(nu*dt - sigma*np.sqrt(dt))
    q = 0.5
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
JR_method(K,T,S0,r,N,sigma,opttype='C')

def EQP_method(K,T,S0,r,N,sigma,opttype='C'):
    #precommute constants
    dt = T/N
    nu = r - 0.5*sigma**2
    dxu = 0.5*nu*dt+0.5*np.sqrt(4*sigma**2*dt-3*nu**2*dt**2)
    dxd = 1.5*nu*dt-0.5*np.sqrt(4*sigma**2*dt-3*nu**2*dt**2)
    pu = 0.5
    pd = 1-pu
    disc = np.exp(-r*dt)
    
    # initialise asset prices at maturity - Time step N
    S = np.zeros(N+1)
    S[0] = S0*np.exp(N*dxd)
    for j in range(1,N+1):
        S[j] = S[j-1]*np.exp(dxu-dxd)
        
    # initialise option values at maturity
    C = np.zeros(N+1)
    for j in range(0,N+1):
        C[j] = max(0,S[j]-K)
        
    # step backwards through tree
    for i in np.arange(N,0,-1):
        for j in range(0,i):
            C[j] = disc * (pu*C[j+1] + pd*C[j])
            
    return C[0]
EQP_method(K,T,S0,r,N,sigma,opttype='C')

def TRG_method(K,T,S0,r,N,sigma,opttype='C'):
    #precommute constants
    dt = T/N
    nu = r - 0.5*sigma**2
    dxu = np.sqrt(sigma**2*dt+nu**2*dt**2)
    dxd = -dxu
    pu = 0.5 + 0.5* nu*dt/dxu
    pd = 1-pu
    disc = np.exp(-r*dt)
    
    # initialise asset prices at maturity - Time step N
    S = np.zeros(N+1)
    S[0] = S0*np.exp(N*dxd)
    for j in range(1,N+1):
        S[j] = S[j-1]*np.exp(dxu-dxd)
        
    # initialise option values at maturity
    C = np.zeros(N+1)
    for j in range(0,N+1):
        C[j] = max(0,S[j]-K)
        
    # step backwards through tree
    for i in np.arange(N,0,-1):
        for j in range(0,i):
            C[j] = disc * (pu*C[j+1] + pd*C[j])
            
    return C[0]
TRG_method(K,T,S0,r,N,sigma,opttype='C')

from py_vollib.black_scholes import black_scholes as bs
import matplotlib.pyplot as plt
