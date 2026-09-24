import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp 
import pandas as pd
import math
from scipy.stats import gaussian_kde

''' FUNCTIONS ''' 

def simulateinflow(lam, alpha, dt, dyear):
    size = int(dyear/dt) 
    InflowExp = np.random.exponential(alpha * np.ones(size)) 
    freqUnif = np.random.random(size=size)
    
    Inflow = np.zeros(size)
    
    yesrain = freqUnif<np.tile(lam,size)*dt
    Inflow[yesrain] = InflowExp[yesrain] 
    return Inflow



def simulatewaterbalance(Inflow, nl, h0, dt): 
    
    tmax = len(Inflow); 
    harray = np.zeros(tmax); harray[0] = h0
    Qarray = np.zeros(tmax);
   
    for k in range(1, tmax): 
        
        h0 = harray[k-1]
    
        h1 = h0 + Inflow[k]
    
       
        if h1 - ho > 0:
            q = a * (h1-ho)**2
            
            
        else:
            q = 0
        h2 = max(h1 - nl*dt- q*dt, 10**-20)
      
        harray[k] = h2
        Qarray[k] = q;
        
    return Inflow, harray, Qarray



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
    plt.ylabel('Water depth (m)')

def analyticalResult (C, lam, alpha, nl, ho, linecolor):
    x = np.linspace(1.7, 1.86)
    y = (C/nl)*np.exp(x*(lam/nl-1/alpha)-lam*ho/nl)
    x1 = np.linspace(1.86,2)
    z = -(x1-ho)**b*a/nl

    hyperf = sp.hyp2f1(1, 0.5, 1.5, z)
    
    y1 = (C/(a*(x1-ho)**b+nl))*np.exp(-x1/alpha+(lam/nl)*(x1-ho)*hyperf)
    plt.plot(x, y, color = linecolor)
    plt.plot(x1, y1, color = linecolor, label='analytical')
    plt.xlim(1.77,1.95)
    plt.ylim(0,25)
    plt.legend()


''' MAIN '''
lam = 0.292 # mean inflow freq
alpha = 0.096 # mean inflow depth
dt = 0.01       # day 
dyear = 365 * 100    # days 
ho = 1.86 #outlet height
nl = 0.0067 #non-outlfow loss
h0 = 1.86 #initial depth
b = 2
C = 25731096 #constant in analytical solution for b = 2
a = 19.5 #outflow coefficient for b = 2



Inflow = simulateinflow(lam, alpha, dt, dyear) 
Inflow, harray, Qarray = simulatewaterbalance(Inflow, nl, h0, dt)


# daily flow characterization
timesteponeday = 100 #time step = 0.01
Daily_Q = np.mean(Qarray.reshape(-1, timesteponeday), axis=1)
Daily_h = np.mean(harray.reshape(-1, timesteponeday), axis=1)

Daily_Q = Daily_Q[Daily_Q != 0] # extract the exact flow events Q>0

Daily_I = Inflow[Inflow != 0]


# cumulative error

filename = "AP daily depth.xlsx"
sheetname = 'Sheet1'   

wtrdphdata = pd.read_excel(filename, sheetname) 

N = round(math.log2(len(wtrdphdata)))+1  
hmin, hmax = np.min(wtrdphdata), np.max(wtrdphdata)
hbinedges = np.linspace(hmin, hmax, N+1)

histhfield, _ = np.histogram(wtrdphdata, bins=hbinedges)
histhmodel, _ = np.histogram(harray, bins=hbinedges)
mfield = len(wtrdphdata)
mmodel = len(harray)
phfield = histhfield / mfield  # P for each bin
phmodel = histhmodel / mmodel

errorh = 0.5 * np.sum(np.abs(phfield -phmodel))
print(f"cumulative error for water depth ε = {errorh:.4f} ({errorh*100:.2f}%)")


filename = "AP CP field discharge.xlsx"
sheetname1 = 'AP inflow'   

inflowfield = pd.read_excel(filename, sheetname1)


N = round(math.log2(len(inflowfield)))+1  
IQmin, IQmax = np.min(inflowfield), np.max(inflowfield)
IQbinedges = np.linspace(IQmin, IQmax, N+1)

histIQfield, _ = np.histogram(inflowfield, bins=IQbinedges)
histIQmodel, _ = np.histogram(Daily_I, bins=IQbinedges)
mfield = len(inflowfield)
mmodel = len(Daily_I)
pIQfield = histIQfield / mfield  
pIQmodel = histIQmodel / mmodel

errorI = 0.5 * np.sum(np.abs(pIQfield -pIQmodel))
print(f"cumulative error for Inflow ε = {errorI:.4f} ({errorI*100:.2f}%)")


sheetname2 = 'AP outflow'  


outflowfield = pd.read_excel(filename, sheetname2)


N = round(math.log2(len(outflowfield)))+1  
OQmin, OQmax = np.min(outflowfield), np.max(outflowfield)
OQbinedges = np.linspace(OQmin, OQmax, N+1)

histOQfield, _ = np.histogram(outflowfield, bins=OQbinedges)
histOQmodel, _ = np.histogram(Daily_Q, bins=OQbinedges)
mfield = len(outflowfield)
mmodel = len(Daily_Q)
pOQfield = histOQfield / mfield  
pOQmodel = histOQmodel / mmodel

errorQ = 0.5 * np.sum(np.abs(pOQfield -pOQmodel))
print(f"cumulative error for outflow ε = {errorQ:.4f} ({errorQ*100:.2f}%)")

# calculate field water depth pdf
fldwtr = wtrdphdata.values.ravel()
fldpdf = gaussian_kde(fldwtr)
xinterval = np.linspace(min(fldwtr),max(fldwtr),100)
pdf = fldpdf(xinterval)

# plot simulated histograms analytical sol field data
plot_2hist(harray, 100, 'Water depth (m)')
plt.plot(xinterval, pdf, label= 'field data', color='black')
analyticalResult (C, lam, alpha, nl, ho, linecolor ='red')


# plot time-series
plot_timeseries(harray)



