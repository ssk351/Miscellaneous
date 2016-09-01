from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from itertools import chain
from scipy import interpolate
import pylab
#def flux_calc():
file = 'time_series_aero.nc'
fh = Dataset(file, mode='r')
tsurf = fh.variables['tsurf'][:]

swdntoatsky = fh.variables['swdntoatsky'][:]

swuptoatsky = fh.variables['swuptoatsky'][:]
lwuptoatsky = fh.variables['lwuptoatsky'][:]

swdnsfctsky = fh.variables['swdnsfctsky'][:]
lwdnsfctsky = fh.variables['lwdnsfctsky'][:]

swupsfctsky = fh.variables['swupsfctsky'][:]
lwupsfctsky = fh.variables['lwupsfctsky'][:]


shflx = fh.variables['shflx'][:]
lhflx = fh.variables['lhflx'][:]
snlhflx = fh.variables['snlhflx'][:]

fh.close()
#print(shflx)
#print(lhflx)
toa_flux = swdntoatsky - ( swuptoatsky + lwuptoatsky )
sfc_flux = swdnsfctsky + lwdnsfctsky - ( swupsfctsky + lwupsfctsky + shflx + lhflx + snlhflx )
sfc_rad = swdnsfctsky + lwdnsfctsky - ( swupsfctsky + lwupsfctsky )
tsurf_t=tsurf.T
tsurf_cel = tsurf_t - 273.15
years = np.arange(1850., 1900.,1.)

#------------------------------------------------------------------------------

flat_tsurf  = [val for sublist in tsurf for val in sublist ]
flat_tsurf_1  = [val for sublist in flat_tsurf for val in sublist ]

flat=np.asarray(flat_tsurf_1)
#print(flat.T)
m,b = np.polyfit(years, flat.T, 1) 
print("The slope of tsurf is ",m)
tck=interpolate.splrep(years,flat.T,s=0)
years_new=np.arange(years.min(),years.max(),(years.max())/10000)
Tsurf_new = interpolate.splev(years_new,tck,der=0)

pylab.plot(years_new,Tsurf_new-273.15) 
#pylab.plot(years_new, power_smooth)#, 'yo', years, m*years+b, '--k') 


pylab.xlabel('Years')
pylab.ylabel('Temperature in degree Celsius')
pylab.ylim([12,16])
plt.title('Surface Temperature for Aerosols')
pylab.savefig('tsurf_aero.eps', format='eps', dpi=1000)

#-------------------------------------------------------------------------------

flat_toa  = [val for sublist in toa_flux for val in sublist ]
flat_toa_1  = [val for sublist in flat_toa for val in sublist ]

flat_toa=np.asarray(flat_toa_1)
#print(flat.T)
m,b = np.polyfit(years, flat_toa.T, 1) 
print("The slope of toa flux is ",m)
#pylab.plot(years, flat_toa.T)#, 'yo', years, m*years+b, '--k') 
#pylab.xlabel('Years')
#pylab.ylabel('TOA flux in Watts')
#pylab.ylim([-5.0,5.0])
#plt.title('TOA flux for Aerosols')
#pylab.savefig('toa_aero')

#---------------------------------------------------------------------------------

flat_sfc  = [val for sublist in sfc_flux for val in sublist ]
flat_sfc_1  = [val for sublist in flat_sfc for val in sublist ]

flat_sfc=np.asarray(flat_sfc_1)
#print(flat.T)
m,b = np.polyfit(years, flat_sfc.T, 1) 
print("The slope of sfc flux is ",m)
#pylab.plot(years, flat_sfc.T)#, 'yo', years, m*years+b, '--k') 
#pylab.xlabel('Years')
#pylab.ylabel('SFC flux in Watts')
#pylab.ylim([-5.0,5.0])
#plt.title('SFC Flux for Aerosols')
#pylab.savefig('sfc_aero')

#---------------------------------------------------------------------------------

flat_sfcr  = [val for sublist in sfc_rad for val in sublist ]
flat_sfc_11  = [val for sublist in flat_sfcr for val in sublist ]

flat_sfcrr=np.asarray(flat_sfc_11)
#print(flat.T)
m,b = np.polyfit(years, flat_sfcrr.T, 1) 
print("The slope of sfc flux is ",m)
#pylab.plot(years, flat_sfcrr.T)#, 'yo', years, m*years+b, '--k') 
#pylab.xlabel('Years')
#pylab.ylabel('SFC net radiation in Watts')
#pylab.ylim([-5.0,5.0])
#plt.title('Aerosol Forced SFC Net Radiation')
#pylab.savefig('sfcr_aero')
#print("The average value is ",m*25+b)


#print(flattened)
#print(len(flattened))
#new_tsurf = [i[0] for i in tsurf]
#list(chain.from_iterable(tsurf)
#print(years)
#print(flattened)
