import sys, string
from matplotlib import rc
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
from netCDF4 import num2date, date2num

def writeFile(nlat, nlon, nlev, outfilename):
	location = (outfilename)
	dataset = netCDF4.Dataset(location,'w',format='NETCDF4')
	times = dataset.createDimension('time', None)
	lats = dataset.createDimension('latitude', nlat )
	lons = dataset.createDimension('longitude', nlon)
	levs = dataset.createDimension('level', nlev)
	return dataset


# Load Data
print("loading data ...")
filename=sys.argv[1]
outfilename=sys.argv[2]
dataset = writeFile(148, 720, 19, outfilename)

print("reading date info ...")
yyyy=int(filename[21:25])
mm=int(filename[25:27])
dd=int(filename[27:29])
date=dt.datetime(yyyy,mm,dd)
print("trmm2nc for date",date)

nc_data = netCDF4.Dataset(filename)
lhmean = nc_data.variables['LHMean'][:]

lat =  np.arange(-37. ,37. ,0.5)
lon =  np.arange(-180. ,180. ,0.5)
lev_1 =  np.array([0.25, 0.75])
lev_2 =  np.arange(1.5 ,18.5 ,1)
lev = np.append(lev_1,lev_2)


# write data to file
print("writing data to file ...")
#   create new variables
print("creating new variables ...")
times = dataset.createVariable('time','f8',('time'))
lats = dataset.createVariable('latitude', 'f4',('latitude'))
lons = dataset.createVariable('longitude', 'f4',('longitude'))
levs = dataset.createVariable('level', 'f4',('level'))
lhmeans = dataset.createVariable('lhmean', np.float32,('time', 'level', 'latitude', 'longitude'), fill_value=-9999.9)

lhmeans.long_name = 'Latent Heating Conditional Mean' 
lhmeans.short_name = 'LHMean'
lhmeans.units = 'K/hr'


times.standard_name = 'time'
times.long_name = 'Year AD'
times.units = 'days since 0001-01-01 00:00:00'
times.calendar = 'standard'

lats.standard_name = 'latitude'
lats.long_name = 'latitude'
lats.units = 'degrees_north'
lats.axis = 'Y'

lons.standard_name = 'longitude'
lons.long_name = 'longitude'
lons.units = 'degrees_east'
lons.axis = 'X'

levs.standard_name = 'level'
levs.long_name = 'level'
levs.units = 'km'
levs.axis = 'Z'

dataset.description = "Netcdf file for TRMM 3H25 data by Bhupendra and Manmeet at IITM Pune"
dataset.history = "Created " + t.ctime(t.time())
dataset.source = "http://disc.gsfc.nasa.gov/datacollection/TRMM_3H25_V7.shtml"

lhmean_1 = np.zeros((1,lhmean.shape[0],lhmean.shape[1],lhmean.shape[2]))
lhmean_1[:,:,:,:] = -9999.9
lhmean_1[0,:,:,:] = lhmean[:,:,:]

times[:] = date2num(date,units=times.units,calendar=times.calendar)
lats[:]  = lat
lons[:]  = lon
levs[:]  = lev
lhmeans[:] = lhmean_1
# Usage
# python trmm2nc.py TRMM_3H25.7_mon_3H25.20140201.7A.nc test.nc
