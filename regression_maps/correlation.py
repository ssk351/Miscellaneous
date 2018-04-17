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

f1_name=sys.argv[1]
f2_name=sys.argv[2]
df_1 = pd.read_csv(f1_name,sep=',',header=None)
df_2 = pd.read_csv(f2_name,sep=',',header=None)
data_1_load = df_1.values
data_2_load  = df_2.values
#print(data_1_load[1])
data_1_norm = (data_1_load-np.mean(data_1_load))/np.std(data_1_load)
data_2_norm  = (data_2_load-np.mean(data_2_load))/np.std(data_2_load)
data_1_fl = data_1_norm.flatten()
data_2_fl = data_2_norm.flatten()
data_1 = data_1_fl.tolist()
data_2 = data_2_fl.tolist()
print(pearsonr(data_1,data_2))

sys.exit()

df = pd.DataFrame({'data_1':data_1_fl,'data_2':data_2_fl})
print(df)
print(df.corr())
sys.exit()
data_1 = data_1_fl.tolist()
data_2 = data_2_fl.tolist()
#print(data_1[0])
#print(data_2)
print(linregress(data_1_norm,data_2_norm))
