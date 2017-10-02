import sys, string
from matplotlib import rc
import numpy
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

def writeFile(nlat,nlon):
	location = ('test.nc')
	dataset = netCDF4.Dataset(location,'w',format='NETCDF4')
	times = dataset.createDimension('time', None)
	lats = dataset.createDimension('lat', nlat )
	lons = dataset.createDimension('lon', nlon)
	return dataset

dataset = writeFile(129,135)
# Load Data
print("loading data ...")
nc_data = netCDF4.Dataset('MADA_pdsi_post.nc')
# Coordinates
time = nc_data.variables['time']
lat = nc_data.variables['lat']
lon = nc_data.variables['lon']
pdsi = nc_data.variables['pdsi']


# write data to file
print("writing data to file ...")
#   create new variables
print("creating new variables ...")
times = dataset.createVariable('time','f8',('time'))
lats = dataset.createVariable('lat', 'f4',('lat'))
lons = dataset.createVariable('lon', 'f4',('lon'))
# get attributes
attrs = [time,lat,lon]
attrs_n = [times,lats,lons]
i = 0
for var in attrs:
	for j in var.ncattrs():
		attrs_n[i].setncattr(j,var.getncattr(j))
	i = i+1
#t_pdsi = pdsi
ndv=-999.0
#t_pdsi[t_pdsi==ndv]=numpy.nan
#print(time[:])
#times     = dataset.createVariable('time','f8',('time'))
#lats = dataset.createVariable('lat', 'f4',('lat'))
#lons = dataset.createVariable('lon', 'f4',('lon'))
t_pdsi      = dataset.createVariable('pdsi', numpy.float32,('time', 'lat', 'lon'), fill_value=-999.0)
t_pdsi_mean = dataset.createVariable('pdsi_mean', numpy.float32,('time'), fill_value=-999.0)

#t_pdsi.FillValue = -999.f 
t_pdsi.long_name = 'Palmer Drought Severity Index, Jun-Aug' 
t_pdsi.short_name = 'PDSI_JJA'

t_pdsi_mean.long_name = 'Palmer Drought Severity Index Mean, Jun-Aug' 
t_pdsi_mean.short_name = 'PDSI_JJA_Mean'

times.standard_name = 'time'
times.long_name = 'Year AD' 
times.units = 'years since 0-01-01 00:00:00'
times.calendar = 'standard'

lats.standard_name = 'latitude'
lats.long_name = 'latitude'
lats.units = 'degrees_north'
lats.axis = 'Y'

lons.standard_name = 'longitude'
lons.long_name = 'longitude'
lons.units = 'degrees_east'
lons.axis = ' X'

#pdsi_ndarray = to_np(pdsi)
np_pdsi=numpy.asarray(pdsi)
np_pdsi.flags.writeable = True
#pdsi.setflags(write=1)
np_pdsi[np_pdsi==-999.0]=numpy.nan
np_pdsi_mean = numpy.nanmean(np_pdsi,axis=(1,2))
#print(np_pdsi_mean.shape[0])
#for i in range(pdsi.shape[0]):
#	for j in range(pdsi.shape[1]):
#		for k in range(pdsi.shape[2]):
#			pdsi[i,j,k] =numpy.nan
#print(pdsi.shape[0])

times[:] = time
lats[:]  = lat
lons[:]  = lon
t_pdsi[:] =np_pdsi
t_pdsi_mean[:]=np_pdsi_mean
#print(pdsi.shape[0])
# 0 is the time 1 is lat and 2 is lon

#variables:
#	float pdsi(time, lat, lon) ;
#		pdsi:FillValue = -999.f ;
#		pdsi:long_name = "Palmer Drought Severity Index, Jun-Aug" ;
#		pdsi:short_name = "PDSI_JJA" ;
#	double time(time) ;
#		time:standard_name = "time" ;
#		time:long_name = "Year AD" ;
#		time:units = "years since 0-01-01 00:00:00" ;
#		time:calendar = "standard" ;
#	double lat(lat) ;
#		lat:standard_name = "latitude" ;
#		lat:long_name = "latitude" ;
#		lat:units = "degrees_north" ;
#		lat:axis = "Y" ;
#	double lon(lon) ;
#		lon:standard_name = "longitude" ;
#		lon:long_name = "longitude" ;
#		lon:units = "degrees_east" ;
#		lon:axis = "X" ;

#How to add attributes
##Add global attributes
#f.description = "Example dataset containing one group"
#f.history = "Created " + today.strftime("%d/%m/%y")
#
##Add local attributes to variable instances
#longitude.units = 'degrees east'
#latitude.units = 'degrees north'
#time.units = 'days since Jan 01, 0001'
#temp.units = 'Kelvin'
#levels.units = 'meters'
#temp.warning = 'This data is not real!'
#
