from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from itertools import chain
import pylab
#def flux_calc():
file = 'time_series_diff.nc'
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
pylab.plot(years, flat.T)#, 'yo', years, m*years+b, '--k') 
pylab.xlabel('Years')
pylab.ylabel('Temperature in degree Celsius')
pylab.ylim([-1.,0.])
plt.title('Surface Temperature for Aerosols')
