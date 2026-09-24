import matplotlib.pyplot as plt
import numpy as np
from scipy.special import beta

''' FUNCTIONS ''' 

def simulateoutflow(lam, alpha, dt, dyear):
    size = int(dyear/dt) 
    outflowExp = np.random.exponential(alpha * np.ones(size)) 
    freqUnif = np.random.random(size=size)
    
    outflow = np.zeros(size)
   
    yesrain = freqUnif<np.tile(lam,size)*dt
    outflow[yesrain] = outflowExp[yesrain] 
    return outflow

def simulatemassbalance(outflow, M0, dt, Lambda, phi): 
    
    tmax = len(outflow); 
    Marray = np.zeros(tmax); Marray[0] = M0
    
    
    for k in range(1, tmax): 
       
        M0 = Marray[k-1]
        
        
        M1 = M0 +Lambda*dt
       
        
        M2 = max(M1 - M1/ho*outflow[k]- phi*M1*dt, 10**-20)
        
        Marray[k] = M2
        
    return Marray





def plot_2hist(matrix0, nbins, varname): 
    plt.figure(figsize=(5,3))
    plt.hist(matrix0.flatten(), nbins, density=True, label='model', alpha=0.5)
    
    plt.xlabel(varname)
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()

def plot_timeseries (matrix1): 
    
    plt.figure(figsize=(5,3))
    plt.plot(matrix1.flatten())
    plt.xlabel('Time step')
    plt.ylabel('M [mg/m^2]')
    plt.legend()

def analyticalResult (lam, alpha, Lambda, ho, phi , linecolor):
    x = np.linspace(0, Lambda/phi,100000)
    y = ((Lambda**(-lam/phi-ho/alpha)*phi**(ho/alpha+1))/beta(ho/alpha+1, lam/phi))*x**(ho/alpha)*(Lambda-phi*x)**(lam/phi-1)
    
    plt.plot(x, y, color = linecolor, label='analytical')
    plt.legend()
    

''' MAIN '''
lam = 0.099 # mean outflow freq
alpha = 0.096  # mean outflow depth
dt = 0.01      # day 
dyear = 365*100    # days 
ho = 1.86 #outlet height
M0 = 300 #initial mass
Lambda = 6.926
phi=0.0146323



outflow = simulateoutflow(lam, alpha, dt, dyear)

Marray = simulatemassbalance(outflow, M0, dt, Lambda, phi)


plot_2hist(Marray, 100, 'M [mg/m^2]')
analyticalResult (lam, alpha, Lambda, ho, phi, linecolor ='red')


plot_timeseries(Marray)

plt.show()
