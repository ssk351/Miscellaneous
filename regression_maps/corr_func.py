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
from netcdftime import utime
import scipy.io
import argparse
import datetime as dt
import pandas as pd
from scipy.signal import butter, lfilter, freqz, hilbert
from scipy.stats import linregress, pearsonr
from sklearn import preprocessing
#from seapy import Sea

def corr_coef_pval(data_1_load, data_2_load): 
	data_1_norm = (data_1_load-np.mean(data_1_load))/np.std(data_1_load)
	data_2_norm  = (data_2_load-np.mean(data_2_load))/np.std(data_2_load)
	data_1_fl = data_1_norm.flatten()
	data_2_fl = data_2_norm.flatten()
	data_1 = data_1_fl.tolist()
	data_2 = data_2_fl.tolist()
	coef = pearsonr(data_1, data_2)[0]
	pvalue = pearsonr(data_1, data_2)[1]
	return coef, pvalue
