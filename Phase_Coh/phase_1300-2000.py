import sys, string
from matplotlib import rc, gridspec
import numpy as np
import pylab as pl
import netCDF4
import time as t
import datetime
from dateutil.parser import parse
from pylab import load, meshgrid, title, arange, show
from netcdftime import utime
import scipy.io
import matplotlib as mpl
import argparse
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter
import datetime as dt
import pandas as pd
from scipy.signal import butter, lfilter, freqz, hilbert

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y
def runningMeanFast(x, N):
		return np.convolve(x, np.ones((N,))/N)[(N-1):]

#Loading netcdf data

# Load Data
print("loading data ...")
nc_data = netCDF4.Dataset('draught_india_time_series_1.nc')
# Coordinates
time = nc_data.variables['time'][:]
pdsi_mean = nc_data.variables['pdsi_mean'][:]
ismr_load = pdsi_mean[::-1]
year_load = time[::-1]
year = year_load[0:year_load.shape[0]-5]
ismr = ismr_load[0:ismr_load.shape[0]-5]
df_nino3_load = pd.read_csv('ienso_li.dat', delimiter=',')
nino3_load = df_nino3_load.values
nino3 = nino3_load[399:nino3_load.shape[0]-2,1]

df_aod = pd.read_csv('gao.txt',delimiter=',')
aod_load = df_aod.values
aod = aod_load[798:aod_load.shape[0],1]
year_aod = aod_load[798:aod_load.shape[0],0]
rf = aod*(-20/150)
## Loading the data
#df_ismr_load = pd.read_excel('ismr.xls')
#ismr_load = df_ismr_load.values
#df_nino3_load = pd.read_excel('nino3.xls')
#nino3_load = df_nino3_load.values
##print(ismr_load.shape)
##print(nino3_load.shape)
#ismr_v = ismr_load.flatten()
#nino3 =  nino3_load.flatten()
#
#ismr=ismr_v/10
##y = butter_lowpass_filter(data, cutoff, fs, order)
#N = ismr.shape[0]
#x = np.linspace(1,N,N)
years = year
# Since our work focuses on the inference of phase relations of inter-annual
# oscillations, we low-pass filtered the data in the spectral domain by multiplying the Fourier
# transformation of the data with a hyperbolic tangent, i.e. high frequency variability with
# frequencies higher than 0.7 cycles per year is damped.
# (reference : Maruan 2006)

cutoff = 0.6
fs = 1
order = 6

ismr_filt  = ismr
#ismr_filt  = butter_lowpass_filter(ismr, cutoff, fs, 6)
nino3_filt = nino3
#nino3_filt = butter_lowpass_filter(nino3, cutoff, fs, 6)

# Since our work focuses on the inference of phase relations of inter-annual
# oscillations, we low-pass filtered the data in the spectral domain by multiplying the Fourier
# transformation of the data with a hyperbolic tangent, i.e. high frequency variability with
# frequencies higher than 0.7 cycles per year is damped.
# (reference : Maruan 2006)
### Second order differencing done as per 
### http://robjhyndman.com/talks/RevolutionR/8-Differencing.pdf

ismr_sec_diff = np.diff(ismr_filt, n=2)
nino3_sec_diff = np.diff(nino3_filt, n=2)
#
## running mean with window width 2l + 1 = 13 data points
ismrr  = ismr_sec_diff
#ismrr  = runningMeanFast(ismr_sec_diff,13)
nino3r = nino3_sec_diff
#nino3r = runningMeanFast(nino3_sec_diff,13)

## Embed by Hilbert transformation with phase defined according to Eq. (4.7).
#
ismr_hilbert  = hilbert(ismrr)
nino3_hilbert = hilbert(nino3r)
ismr_real = np.real(ismr_hilbert)
ismr_imag = np.imag(ismr_hilbert)
nino3_real = np.real(nino3_hilbert)
nino3_imag = np.imag(nino3_hilbert)
ismr_A = np.abs(ismr_hilbert)
nino3_A = np.abs(nino3_hilbert)
phi_ismr  = np.arctan(ismr_imag/ismr_real) 
phi_nino3 = np.arctan(nino3_imag/nino3_real)
# In the polar plot the x axis is Nino3 and y axis is absolute part of hilbert transform
#http://circ.ahajournals.org/content/114/6/536.full
#
# Phase unwrapped as per
# https://in.mathworks.com/matlabcentral/answers/295635-why-the-phase-obtained-with-hilbert-transform-and-phase-unwrap-is-different-from-the-actual-phase
#
phase_ismr = np.unwrap(np.angle(ismr_hilbert))
phase_nino3 = np.unwrap(np.angle(nino3_hilbert))
#
phase_coh = phase_ismr - phase_nino3

fig = pl.figure(figsize=(10,10))
gs = gridspec.GridSpec(2,1)
ax1=fig.add_subplot(gs[0,0]) # Second row, span all columns
ax1.plot(years[2:703],-phase_coh/(2*np.pi))
ax1.set_xlabel('years')
ax1.set_ylabel('Phase coherence')
ax1.set_title('Phase coherence between ISMR and NINO3 1300-2002')
pl.grid()

ax2=fig.add_subplot(gs[1,0])
ax2.plot(year_aod,rf)
ax2.set_ylabel('Radiative Forcing')
ax2.set_xlabel('years')
ax2.set_title('Gao dataset using 54 ice cores 500-2002')

fig.savefig('test.png')




