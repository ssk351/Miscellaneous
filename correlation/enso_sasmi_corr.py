import sys, string
from matplotlib import rc, gridspec
import numpy as np
import matplotlib as mpl
mpl.use('agg')
import pylab as pl
import netCDF4
import time as t
from datetime import datetime, timedelta, date
from dateutil.parser import parse
from pylab import load, meshgrid, title, arange, show
from netcdftime import utime
import scipy.io
import argparse
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter
import datetime as dt
import pandas as pd
from scipy.signal import butter, lfilter, freqz, hilbert
from scipy.stats import linregress, pearsonr
from sklearn import preprocessing
#from seapy import Sea

df_sasmi = pd.read_csv('sasmi_900_2002_2.txt',sep='\t',header=None)
df_enso = pd.read_csv('enso_900_2002_2.txt',sep=',',header=None)
sasmi_load = df_sasmi.values
enso_load  = df_enso.values
#print(sasmi_load[1])
sasmi_norm = (sasmi_load-np.mean(sasmi_load))/np.std(sasmi_load)
enso_norm  = (enso_load-np.mean(enso_load))/np.std(enso_load)
sasmi_fl = sasmi_norm.flatten()
enso_fl = enso_norm.flatten()
sasmi = sasmi_fl.tolist()
enso = enso_fl.tolist()
print(pearsonr(sasmi,enso))

sys.exit()

df = pd.DataFrame({'sasmi':sasmi_fl,'enso':enso_fl})
print(df)
print(df.corr())
sys.exit()
sasmi = sasmi_fl.tolist()
enso = enso_fl.tolist()
#print(sasmi[0])
#print(enso)
print(linregress(sasmi_norm,enso_norm))
