import numpy as np
import pandas as pd
import math

# cumulative error for AP

filename = "AP daily depth.xlsx"
sheetname = 'Sheet1'   
harray = np.load("modelh AP.npy")
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
print(f"cumulative error for water depth in AP (b=2) ε = {errorh:.4f} ({errorh*100:.2f}%)")

harray = np.load("modelh3 AP.npy")
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
print(f"cumulative error for water depth in AP (b=3) ε = {errorh:.4f} ({errorh*100:.2f}%)")

filename = "AP CP field discharge.xlsx"
sheetname1 = 'AP inflow'   
Daily_I = np.load("modelI AP.npy")
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
print(f"cumulative error for Inflow in AP ε = {errorI:.4f} ({errorI*100:.2f}%)")


sheetname2 = 'AP outflow'  
Daily_Q = np.load("modelQ AP.npy")
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
print(f"cumulative error for outflow in AP ε = {errorQ:.4f} ({errorQ*100:.2f}%)")


# cumulative error for CP

filename = "CP daily depth.xlsx"
sheetname = 'Sheet1'   
harray = np.load("modelh CP.npy")
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
print(f"cumulative error for water depth in CP (b=2) ε = {errorh:.4f} ({errorh*100:.2f}%)")

harray = np.load("modelh3 CP.npy")
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
print(f"cumulative error for water depth in CP (b=3) ε = {errorh:.4f} ({errorh*100:.2f}%)")

filename = "AP CP field discharge.xlsx"
sheetname1 = 'CP inflow'   
Daily_I = np.load("modelI CP.npy")
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
print(f"cumulative error for Inflow in CP ε = {errorI:.4f} ({errorI*100:.2f}%)")


sheetname2 = 'CP outflow'  
Daily_Q = np.load("modelQ CP.npy")
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
print(f"cumulative error for outflow in CP ε = {errorQ:.4f} ({errorQ*100:.2f}%)")