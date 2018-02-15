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
#import Nio
from pyhdf.SD import SD

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
yyyy=int(filename[78:82])
mm=int(filename[82:84])
dd=int(filename[84:86])
date=dt.datetime(yyyy,mm,dd)
print("trmm2nc for date",date)

print(filename)

#sys.exit()
#lhmean = hf.variables['LHMean'] 
hf = SD(filename)
sds_1 = hf.select("LHMean")
lhmean = sds_1.get()
#print(lhmean.shape)

sds_2 = hf.select("convLHMean")
convlhmean = sds_2.get()
#print(convlhmean.shape)

sds_3 = hf.select("stratLHMean")
stratlhmean = sds_3.get()
#print(stratlhmean.shape)

sds_4 = hf.select("shallowLHMean")
shallowlhmean = sds_4.get()
#print(shallowlhmean.shape)

sds_5 = hf.select("Q1RMean")
q1rmean = sds_5.get()
#print(q1rmean.shape)

sds_6 = hf.select("convQ1RMean")
convq1rmean = sds_6.get()
#print(convq1rmean.shape)

sds_7 = hf.select("stratQ1RMean")
stratq1rmean = sds_7.get()
#print(stratq1rmean.shape)

sds_8 = hf.select("shallowQ1RMean")
shallowq1rmean = sds_8.get()
#print(shallowq1rmean.shape)

sds_9 = hf.select("Q2Mean")
q2mean = sds_9.get()
#print(q2mean.shape)

sds_10 = hf.select("convQ2Mean")
convq2mean = sds_10.get()
#print(convq2mean.shape)

sds_11 = hf.select("stratQ2Mean")
stratq2mean = sds_11.get()
#print(stratq2mean.shape)

sds_12 = hf.select("shallowQ2Mean")
shallowq2mean = sds_12.get()
#print(shallowq2mean.shape)

sds_13 = hf.select("allPix")
allpix = sds_13.get()
#print(allpix.shape)

sds_14 = hf.select("convPix")
convpix = sds_14.get()
#print(convpix.shape)

sds_15 = hf.select("stratPix")
stratpix = sds_15.get()
#print(stratpix.shape)

sds_16 = hf.select("shallowPix")
shallowpix = sds_16.get()
#print(shallowpix.shape)




#print(lhmean.shape)
##print(lhmean)
#print(lhmean.shape)
#sys.exit()
lat =  np.arange(-36.75 ,37. ,0.5)
lon =  np.arange(-179.75 ,180. ,0.5)
lev_1 =  np.array([0.25, 0.75])
lev_2 =  np.arange(1.5 ,18.5 ,1)
lev = np.append(lev_1,lev_2)
print(lat)
print(lon)
sys.exit()
# write data to file
print("writing data to file ...")
#   create new variables
print("creating new variables ...")
times = dataset.createVariable('time','f8',('time'))
lats = dataset.createVariable('latitude', 'f4',('latitude'))
lons = dataset.createVariable('longitude', 'f4',('longitude'))
levs = dataset.createVariable('level', 'f4',('level'))

lhmeans           = dataset.createVariable('lhmean', np.float32,('time', 'level','longitude', 'latitude'), fill_value=-9999.9)
convlhmeans       = dataset.createVariable('convlhmean', np.float32,('time', 'level','longitude', 'latitude'), fill_value=-9999.9)
stratlhmeans      = dataset.createVariable('stratlhmean', np.float32,('time', 'level','longitude', 'latitude'), fill_value=-9999.9)
shallowlhmeans    = dataset.createVariable('shallowlhmean', np.float32,('time', 'level','longitude', 'latitude'), fill_value=-9999.9)
q1rmeans          = dataset.createVariable('q1rmean', np.float32,('time', 'level','longitude', 'latitude'), fill_value=-9999.9)
convq1rmeans      = dataset.createVariable('convq1rmean', np.float32,('time', 'level','longitude', 'latitude'), fill_value=-9999.9)
stratq1rmeans     = dataset.createVariable('stratq1rmeans', np.float32,('time', 'level','longitude', 'latitude'), fill_value=-9999.9)
shallowq1rmeans   = dataset.createVariable('shallowq1rmean', np.float32,('time', 'level','longitude', 'latitude'), fill_value=-9999.9)
q2means           = dataset.createVariable('q2mean', np.float32,('time', 'level','longitude', 'latitude'), fill_value=-9999.9)
convq2means       = dataset.createVariable('convq2mean', np.float32,('time', 'level','longitude', 'latitude'), fill_value=-9999.9)
stratq2means      = dataset.createVariable('stratq2mean', np.float32,('time', 'level','longitude', 'latitude'), fill_value=-9999.9)
shallowq2means    = dataset.createVariable('shallowq2mean', np.float32,('time', 'level','longitude', 'latitude'), fill_value=-9999.9)
allpixs     		  = dataset.createVariable('allpix', np.float32,('time', 'level','longitude', 'latitude'), fill_value=-9999.9)
convpixs    		  = dataset.createVariable('convpix', np.float32,('time', 'level','longitude', 'latitude'), fill_value=-9999.9)
stratpixs   		  = dataset.createVariable('stratpix', np.float32,('time', 'level','longitude', 'latitude'), fill_value=-9999.9)
shallowpixs 		  = dataset.createVariable('shallowpix', np.float32,('time', 'level','longitude', 'latitude'), fill_value=-9999.9)

lhmeans.long_name = 'Latent Heating Conditional Mean' 
lhmeans.short_name = 'LHMean'
lhmeans.units = 'K/hr'

convlhmeans.long_name = 'Convective Latent Heating Conditional Mean' 
convlhmeans.short_name = 'convLHMean'
convlhmeans.units = 'K/hr'

stratlhmeans.long_name = 'Stratiform Latent Heating Conditional Mean' 
stratlhmeans.short_name = 'stratLHMean'
stratlhmeans.units = 'K/hr'

q1rmeans.long_name = 'Q1R Latent Heating Conditional Mean' 
q1rmeans.short_name = 'Q1RMean'
q1rmeans.units = 'K/hr'
#
#shallowlhmeans.long_name = 'Latent Heating Conditional Mean' 
#shallowlhmeans.short_name = 'LHMean'
#shallowlhmeans.units = 'K/hr'
#
#convq1rmeans.long_name = 'Latent Heating Conditional Mean' 
#convq1rmeans.short_name = 'LHMean'
#convq1rmeans.units = 'K/hr'
#
#stratq1rmeans.long_name = 'Latent Heating Conditional Mean' 
#stratq1rmeans.short_name = 'LHMean'
#stratq1rmeans.units = 'K/hr'
#
#q2means.long_name = 'Latent Heating Conditional Mean' 
#q2means.short_name = 'LHMean'
#q2means.units = 'K/hr'
#
#convq2means.long_name = 'Latent Heating Conditional Mean' 
#convq2means.short_name = 'LHMean'
#convq2means.units = 'K/hr'
#
#stratq2means.long_name = 'Latent Heating Conditional Mean' 
#stratq2means.short_name = 'LHMean'
#stratq2means.units = 'K/hr'
#
#shallowq2means.long_name = 'Latent Heating Conditional Mean' 
#shallowq2means.short_name = 'LHMean'
#shallowq2means.units = 'K/hr'
#
#allpixs.long_name = 'Latent Heating Conditional Mean' 
#allpixs.short_name = 'LHMean'
#allpixs.units = 'K/hr'
#
#convpixs.long_name = 'Latent Heating Conditional Mean' 
#convpixs.short_name = 'LHMean'
#convpixs.units = 'K/hr'
#
#stratpixs.long_name = 'Latent Heating Conditional Mean' 
#stratpixs.short_name = 'LHMean'
#stratpixs.units = 'K/hr'
#
#shallowpixs.long_name = 'Latent Heating Conditional Mean' 
#shallowpixs.short_name = 'LHMean'
#shallowpixs.units = 'K/hr'

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
convlhmean_1      = np.zeros((1,lhmean.shape[0],lhmean.shape[1],lhmean.shape[2]))
stratlhmean_1     = np.zeros((1,lhmean.shape[0],lhmean.shape[1],lhmean.shape[2]))
shallowlhmean_1   = np.zeros((1,lhmean.shape[0],lhmean.shape[1],lhmean.shape[2]))
q1rmean_1         = np.zeros((1,lhmean.shape[0],lhmean.shape[1],lhmean.shape[2]))
convq1rmean_1     = np.zeros((1,lhmean.shape[0],lhmean.shape[1],lhmean.shape[2]))
stratq1rmean_1    = np.zeros((1,lhmean.shape[0],lhmean.shape[1],lhmean.shape[2]))
shallowq1rmean_1  = np.zeros((1,lhmean.shape[0],lhmean.shape[1],lhmean.shape[2]))
q2mean_1          = np.zeros((1,lhmean.shape[0],lhmean.shape[1],lhmean.shape[2]))
convq2mean_1      = np.zeros((1,lhmean.shape[0],lhmean.shape[1],lhmean.shape[2]))
stratq2mean_1     = np.zeros((1,lhmean.shape[0],lhmean.shape[1],lhmean.shape[2]))
shallowq2mean_1   = np.zeros((1,lhmean.shape[0],lhmean.shape[1],lhmean.shape[2]))
allpix_1     		 = np.zeros((1,lhmean.shape[0],lhmean.shape[1],lhmean.shape[2]))
convpix_1    		 = np.zeros((1,lhmean.shape[0],lhmean.shape[1],lhmean.shape[2]))
stratpix_1   		 = np.zeros((1,lhmean.shape[0],lhmean.shape[1],lhmean.shape[2]))
shallowpix_1 		 = np.zeros((1,lhmean.shape[0],lhmean.shape[1],lhmean.shape[2]))

lhmean_1[:,:,:,:] = -9999.9
convlhmean_1[:,:,:,:] = -9999.9
stratlhmean_1[:,:,:,:] = -9999.9
shallowlhmean_1[:,:,:,:] = -9999.9
q1rmean_1[:,:,:,:] = -9999.9
convq1rmean_1[:,:,:,:] = -9999.9
stratq1rmean_1[:,:,:,:] = -9999.9
shallowq1rmean_1[:,:,:,:] = -9999.9
q2mean_1[:,:,:,:] = -9999.9
convq2mean_1[:,:,:,:] = -9999.9
stratq2mean_1[:,:,:,:] = -9999.9
shallowq2mean_1[:,:,:,:] = -9999.9
allpix_1[:,:,:,:] = -9999.9
convpix_1[:,:,:,:] = -9999.9
stratpix_1[:,:,:,:] = -9999.9
shallowpix_1[:,:,:,:] = -9999.9


lhmean_1[0,:,:,:]           = lhmean[:,:,:]
convlhmean_1[0,:,:,:]       = convlhmean[:,:,:]
stratlhmean_1[0,:,:,:]      = stratlhmean[:,:,:]
shallowlhmean_1[0,:,:,:]    = shallowlhmean[:,:,:]
q1rmean_1[0,:,:,:]          = q1rmean[:,:,:]
convq1rmean_1[0,:,:,:]      = convq1rmean[:,:,:]
stratq1rmean_1[0,:,:,:]     = stratq1rmean[:,:,:]
shallowq1rmean_1[0,:,:,:]   = shallowq1rmean[:,:,:]
q2mean_1[0,:,:,:]           = q2mean[:,:,:]
convq2mean_1[0,:,:,:]       = convq2mean[:,:,:]
stratq2mean_1[0,:,:,:]      = stratq2mean[:,:,:]
shallowq2mean_1[0,:,:,:]    = shallowq2mean[:,:,:]
allpix_1[0,:,:,:]           = allpix[:,:,:]
convpix_1[0,:,:,:]          = convpix[:,:,:]
stratpix_1[0,:,:,:]         = stratpix[:,:,:]
shallowpix_1[0,:,:,:]       = shallowpix[:,:,:]





times[:] = date2num(date,units=times.units,calendar=times.calendar)
lats[:]  = lat
lons[:]  = lon
levs[:]  = lev
lhmeans[:]         = lhmean_1
convlhmeans[:]     = convlhmean_1     
stratlhmeans[:]    = stratlhmean_1    
shallowlhmeans[:]  = shallowlhmean_1  
q1rmeans[:]        = q1rmean_1        
convq1rmeans[:]    = convq1rmean_1    
stratq1rmeans[:]   = stratq1rmean_1   
shallowq1rmeans[:] = shallowq1rmean_1 
q2means[:]         = q2mean_1         
convq2means[:]     = convq2mean_1     
stratq2means[:]    = stratq2mean_1    
shallowq2means[:]  = shallowq2mean_1  
allpixs[:]         = allpix_1     		 
convpixs[:]        = convpix_1    		 
stratpixs[:]       = stratpix_1   		 
shallowpixs[:]     = shallowpix_1 		 





#      float LHMean ( nlayer, nlon, nlat )
#         units :	K/hr
#         hdf_name :	LHMean
#      float convLHMean ( nlayer, nlon, nlat )
#         units :	K/hr
#         hdf_name :	convLHMean
#      float stratLHMean ( nlayer, nlon, nlat )
#         units :	K/hr
#         hdf_name :	stratLHMean
#      float shallowLHMean ( nlayer, nlon, nlat )
#         units :	K/hr
#         hdf_name :	shallowLHMean
#      float Q1RMean ( nlayer, nlon, nlat )
#         units :	K/hr
#         hdf_name :	Q1RMean
#      float convQ1RMean ( nlayer, nlon, nlat )
#         units :	K/hr
#         hdf_name :	convQ1RMean
#      float stratQ1RMean ( nlayer, nlon, nlat )
#         units :	K/hr
#         hdf_name :	stratQ1RMean
#      float shallowQ1RMean ( nlayer, nlon, nlat )
#         units :	K/hr
#         hdf_name :	shallowQ1RMean
#      float Q2Mean ( nlayer, nlon, nlat )
#         units :	K/hr
#         hdf_name :	Q2Mean
#      float convQ2Mean ( nlayer, nlon, nlat )
#         units :	K/hr
#         hdf_name :	convQ2Mean
#      float stratQ2Mean ( nlayer, nlon, nlat )
#         units :	K/hr
#         hdf_name :	stratQ2Mean
#      float shallowQ2Mean ( nlayer, nlon, nlat )
#         units :	K/hr
#         hdf_name :	shallowQ2Mean
#      float allPix ( nlayer, nlon, nlat )
#         hdf_name :	allPix
#      float convPix ( nlayer, nlon, nlat )
#         hdf_name :	convPix
#      float stratPix ( nlayer, nlon, nlat )
#         hdf_name :	stratPix
#      float shallowPix ( nlayer, nlon, nlat )
#         hdf_name :	shallowPix

# Usage
# python trmm2hdf.py TRMM_3H25.7_mon_3H25.20140201.7A.HDF test_hdf.nc
